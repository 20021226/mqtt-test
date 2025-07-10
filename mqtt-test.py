import logging
import paho.mqtt.client as mqtt
import json
import time
import traceback
from typing import Dict, Any, List
from config import MQTT_CONFIG, STATE_DEFINITIONS, TYPE_MAPPING, DEVICE
import db_operations as db

def parse_device_message(raw_message: Dict[str, Any], module_number: int = 1) -> list:
    """
    解析原始设备消息，生成固定格式的记录列表
    
    :param raw_message: 原始消息字典
    :param module_number: 模块编号
    :return: 格式化后的记录列表
    """
    records = []
    
    # 检查原始消息格式
    if "time" not in raw_message or "data" not in raw_message:
        print("Invalid message format: missing 'time' or 'data' field")
        return records
    
    # 遍历所有数据项
    for data_item in raw_message["data"]:
        # 获取类型和状态数据
        item_type = data_item.get("type")
        state_data = data_item.get("state")
        
        if item_type is None or state_data is None:
            continue
        
        # 获取类型名称
        type_name = TYPE_MAPPING.get(item_type, "other")
        
        # 获取该类型的状态定义
        type_definitions = STATE_DEFINITIONS.get(type_name)
        if not type_definitions:
            continue
    
        # 根据不同类型处理状态数据
        if type_name == "bms":
            # BMS状态使用索引直接获取值
            for code, definition in type_definitions.items():
                index = definition.get("index")
                if index is not None and index < len(state_data):
                    value = state_data[index]
                    records.append(create_record(code, value, definition, type_name, module_number))
        elif type_name == "liquidCoolingFaults":
            # 液冷故障状态使用索引直接获取值
            for code, definition in type_definitions.items():
                if len(state_data) > 0:
                    value = state_data[0]
                else:
                    value = 0
                    logging.warning(f'state_data 为空')
                # 检查位值是否在定义中
                number = definition.get('number', None)
                # 默认正常 0
                values = 0
                if number==value:
                    values=1
                records.append(create_record(code, values, definition, type_name, module_number))              
        elif type_name == "airConditioner":
            # 空调状态，每8位表示一个类型，数组索引0表示byte1，索引1表示byte2
            for byte_name, byte_definitions in type_definitions.items():
                # 确定数组索引
                array_index = 0  # 默认为byte1 (索引0)
                
                if byte_name == "byte2":
                    array_index = 1
                elif byte_name == "byte3":
                    array_index = 2
                elif byte_name == "byte4":
                    array_index = 3
                
                # 检查数组索引是否有效
                if array_index < len(state_data):
                    # 遍历当前字节的所有位定义
                    for field_name, definition in byte_definitions.items():
                        bit = definition.get("bit")
                        if bit is None:
                            continue
                        
                        # 使用8位宽度获取位值
                        value = (state_data[array_index] >> bit) & 1
                        
                        # 创建完整的code标识符
                        code = f"{field_name}"
                        
                        if value is not None:
                            records.append(create_record(code, value, definition, type_name, module_number))
        elif type_name == "bmsFaults":
            # bmsFaults每4个字节表示一个类型，最后一个使用2个字节
            for sub_type, sub_definitions in type_definitions.items():
                # 确定子类型的起始索引
                start_index = 0
                if sub_type == "moderateAlarms":
                    start_index = 4
                elif sub_type == "seriousAlarms":
                    start_index = 8
                elif sub_type == "faults":
                    start_index = 12
                
                # 检查数组长度是否足够
                if start_index + 4 > len(state_data):
                    continue
                
                # 处理每个子类型的定义
                for code, definition in sub_definitions.items():
                    bit = definition.get("bit")
                    if bit is None:
                        continue
                    
                    # 计算实际的数组索引和位偏移
                    element_index = bit // 32  # 每个元素32位
                    bit_offset = bit % 32
                    
                    # 检查元素索引是否有效
                    if element_index < 4:  # 最多4个元素
                        array_index = start_index + element_index
                        if array_index < len(state_data):
                            value = (state_data[array_index] >> bit_offset) & 1
                            if value is not None:
                                records.append(create_record(code, value, definition, f"{type_name}.{sub_type}", module_number))
        elif type_name == "pcsFaults":
            # pcsFaults每个类型使用2个字节表示，相当于数组的两个元素
            for element_key, element_definitions in type_definitions.items():
                try:
                    element_index = int(element_key) - 1  # 元素索引从0开始，但定义从1开始
                    base_index = element_index * 2  # 每个元素占用2个数组位置
                    
                    # 检查数组长度是否足够
                    if base_index + 1 >= len(state_data):
                        continue
                    
                    # 处理每个元素的定义
                    for code, definition in element_definitions.items():
                        bit = definition.get("bit")
                        if bit is None:
                            continue
                        
                        # 计算16位值
                        word_value = (state_data[base_index + 1] << 8) | state_data[base_index]
                        value = (word_value >> bit) & 1
                        
                        if value is not None:
                            records.append(create_record(code, value, definition, type_name, module_number))
                except (ValueError, IndexError):
                    continue
        elif type_name == "dcdcFaults":
            # dcdcFaults每个类型使用1个字节表示，相当于数组的一个元素
            for byte_key, byte_definitions in type_definitions.items():
                # 确定字节索引
                try:
                    byte_num = int(byte_key.replace("byte", ""))
                    array_index = byte_num - 1  # 数组索引从0开始，但byte从1开始
                    
                    # 检查数组长度是否足够
                    if array_index >= len(state_data):
                        continue
                    
                    # 处理每个字节的定义
                    for code, definition in byte_definitions.items():
                        bit = definition.get("bit")
                        if bit is None:
                            continue
                        
                        # 使用8位宽度获取位值
                        value = (state_data[array_index] >> bit) & 1
                        if value is not None:
                            records.append(create_record(code, value, definition, type_name, module_number))
                except (ValueError, IndexError):
                    continue
        else:
            # 其他状态使用位操作解析
            for code, definition in type_definitions.items():
                bit = definition.get("bit")
                if bit is None:
                    continue
                
                # 获取位值
                value = get_bit_value(state_data, bit)
                if value is not None:
                    # 创建记录
                    records.append(create_record(code, value, definition, type_name, module_number))
    
    return records

def get_bit_value(state_data, bit, bit_width=8):
    # 根据位宽计算索引和偏移
    if bit_width == 8:  # 字节
        index = bit // 8
        offset = bit % 8
    elif bit_width == 16:  # 字
        index = bit // 16
        offset = bit % 16
    elif bit_width == 32:  # 双字
        index = bit // 32
        offset = bit % 32
    else:
        logging.error(f"不支持的位宽: {bit_width}")
        return None
    
    if index < len(state_data):
        return (state_data[index] >> offset) & 1
    return None

def create_record(code: str, value: int, definition: Dict[str, Any], type_name: str, module_number: int) -> Dict[str, Any]:
    """
    创建单个状态记录
    
    :param code: 状态代码
    :param value: 状态值
    :param definition: 状态定义
    :param type_name: 类型名称
    :param module_number: 模块编号
    :return: 格式化后的记录
    """
    # 获取值描述
    value_desc = definition["values"].get(value, "未知")
    
    # 判断是否正常
    normal_value = definition.get("normal_value")
    is_normal = True if normal_value is None else (value == normal_value)
    
    # 构建描述
    desc = f"{definition['desc']}：{value}-{value_desc}"
    
    # 返回记录
    return {
        "code": code,
        "value": value,
        "desc": desc,
        "normal": is_normal,
        "type": type_name,
        "module_number": module_number
    }

def on_connect(client, userdata, flags, rc):
    """MQTT 连接回调"""
    if rc == 0:
        print("Connected to MQTT broker successfully!")
        # 订阅主题 (根据实际需求修改主题)
        client.subscribe(f"GLOBALPOWER/{DEVICE.DEVICE_ID}/STATE_FAULT_DATA/{DEVICE.DEVICE_MODULE}", qos=MQTT_CONFIG["qos"])
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    """MQTT 消息接收回调"""
    try:
        print(f"Received message from topic {msg.topic}")
        
        # 解析 JSON 消息
        payload = msg.payload.decode("utf-8")
        message_data = json.loads(payload)
        
        # 获取时间戳
        timestamp = message_data.get("time", int(time.time()))
        
        # 解析设备消息 (假设模块编号可以从主题或消息中获取)
        parsed_records = parse_device_message(message_data, DEVICE.DEVICE_MODULE)
        
        if parsed_records:
            print(f"Parsed {len(parsed_records)} records:")
            for record in parsed_records:
                print(json.dumps(record, indent=4, ensure_ascii=False))
                print("---")
            
            # 保存记录到数据库
            conn = db.init_database()
            db.save_records(conn, parsed_records, timestamp)
            conn.close()
        else:
            print("No records parsed from message")
            
    except Exception as e:
        print(f"Error processing message: {str(e)}")
        traceback.print_exc()

def setup_mqtt_client():
    """设置并返回 MQTT 客户端"""
    client = mqtt.Client()
    client.username_pw_set(MQTT_CONFIG["account"], MQTT_CONFIG["password"])
    client.on_connect = on_connect
    client.on_message = on_message
    
    return client

def main():
    # 默认启动MQTT客户端
    client = setup_mqtt_client()
    try:
        # 连接 MQTT 服务器
        client.connect(MQTT_CONFIG["ip"], MQTT_CONFIG["port"], 60)
        
        # 保持连接并处理消息
        client.loop_forever()
        
    except KeyboardInterrupt:
        print("Disconnecting from MQTT broker...")
        client.disconnect()
    except Exception as e:
        print(f"MQTT error: {str(e)}")
        client.disconnect()

if __name__ == "__main__":
    main()