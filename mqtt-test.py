import paho.mqtt.client as mqtt
import json
import time
import sys
import argparse
from typing import Dict, Any, List
from config import MQTT_CONFIG, STATE_DEFINITIONS, TYPE_MAPPING
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

def get_bit_value(state_data: list, bit: int) -> int:
    """
    从状态数据中获取指定位的值
    
    :param state_data: 状态数据列表
    :param bit: 位索引
    :return: 位值，如果无法获取则返回None
    """
    # 计算位所在的字节索引和位偏移
    byte_index = bit // 8
    bit_offset = bit % 8
    
    # 确保状态数据长度足够
    if byte_index < len(state_data):
        # 获取对应字节的值
        byte_value = state_data[byte_index]
        
        # 提取对应位的值
        return (byte_value >> bit_offset) & 1
    
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
        client.subscribe("GLOBALPOWER/FZAUS0000001/STATE_FAULT_DATA/1", qos=MQTT_CONFIG["qos"])
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
        module_number = 1  # 这里需要根据实际情况获取模块编号
        parsed_records = parse_device_message(message_data, module_number)
        
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
        import traceback
        traceback.print_exc()



def setup_mqtt_client():
    """设置并返回 MQTT 客户端"""
    client = mqtt.Client()
    client.username_pw_set(MQTT_CONFIG["account"], MQTT_CONFIG["password"])
    client.on_connect = on_connect
    client.on_message = on_message
    
    return client

def test_parse_message():
    """
    测试解析消息功能并保存到数据库
    """
    # 测试数据
    test_message = {
        "time": 1751961896,
        "data": [
            {
                "type": 0,
                "state": [32, 0]
            },
            {
                "type": 1,
                "state": [0, 0]
            },
            {
                "type": 2,
                "state": [3, 0, 0]
            },
            {
                "type": 3,
                "state": [0, 0]
            },
            {
                "type": 4,
                "state": [0, 0, 0, 0]
            },
            {
                "type": 5,
                "state": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            },
            {
                "type": 6,
                "state": [0, 0, 0, 0, 0, 0, 0, 0]
            },
            {
                "type": 7,
                "state": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            },
            {
                "type": 8,
                "state": [0]
            }
        ]
    }
    
    # 获取时间戳
    timestamp = test_message.get("time", int(time.time()))
    
    # 解析消息
    records = parse_device_message(test_message)
    
    # 打印结果
    print(f"解析结果: 共 {len(records)} 条记录")
    for record in records:
        print(json.dumps(record, indent=4, ensure_ascii=False))
        print("---")
    
    # 保存到数据库
    if records:
        print("正在保存记录到数据库...")
        conn = db.init_database()
        db.save_records(conn, records, timestamp)
        
        # 查询并显示保存的记录数量
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM device_records")
        count = cursor.fetchone()[0]
        print(f"数据库中共有 {count} 条记录")
        
        conn.close()




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