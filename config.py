# MQTT 配置
MQTT_CONFIG = {
    "account": "AUS_platform",
    "password": "AUS_platform",
    "ip": "139.224.223.35",
    "port": 1883,
    "qos": 2
}

# 状态定义映射表
STATE_DEFINITIONS = {
    # 系统状态 (type=0)
    "system": {
        "lightningProtectorState": {"bit": 0, "desc": "防雷器状态", "values": {0: "正常", 1: "动作"}, "normal_value": 0},
        "incomingSwitchState": {"bit": 1, "desc": "进线开关状态", "values": {0: "断开", 1: "闭合"}, "normal_value": None},
        "accessControlState": {"bit": 2, "desc": "门禁状态", "values": {0: "关闭", 1: "打开"}, "normal_value": None},
        "runStat": {"bit": 3, "desc": "运行状态", "values": {0: "正常", 1: "异常"}, "normal_value": 0},
        "pcsFault": {"bit": 4, "desc": "PCS通信故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
        "bmsFault": {"bit": 5, "desc": "BMS通信故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
        "fourInOneSensorCommunicationFault": {"bit": 6, "desc": "四合一传感器通信故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
        "airConditionerFault": {"bit": 7, "desc": "空调通信故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
        "energyMeterFault": {"bit": 8, "desc": "柜内电表通讯故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
        "lemsFault": {"bit": 9, "desc": "lems故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
        "electricityMode": {"bit": 10, "desc": "用电方式", "values": {0: "电网", 1: "柴发"}, "normal_value": None}
    },
    # PCS状态 (type=1)
    "pcs": {
        "haltState": {"bit": 0, "desc": "停机状态", "values": {0: "无效", 1: "停机"}, "normal_value": None},
        "standbyState": {"bit": 1, "desc": "待机状态", "values": {0: "无效", 1: "待机"}, "normal_value": None},
        "runState": {"bit": 2, "desc": "运行状态", "values": {0: "无效", 1: "运行"}, "normal_value": None},
        "totalFaultState": {"bit": 3, "desc": "总故障状态", "values": {0: "无效", 1: "故障"}, "normal_value": 0},
        "totalAlarmState": {"bit": 4, "desc": "总告警状态", "values": {0: "无效", 1: "告警"}, "normal_value": 0},
        "telnetLocallyState": {"bit": 5, "desc": "远程/就地状态", "values": {0: "就地", 1: "远程"}, "normal_value": None},
        "scramInputState": {"bit": 6, "desc": "急停输入状态", "values": {0: "无效", 1: "急停"}, "normal_value": 0},
        "mergeNetState": {"bit": 7, "desc": "并网状态", "values": {0: "无效", 1: "并网"}, "normal_value": None},
        "leaveNetState": {"bit": 8, "desc": "离网状态", "values": {0: "无效", 1: "离网"}, "normal_value": None},
        "overloadCapacityReduction": {"bit": 9, "desc": "过载降容", "values": {0: "未过载", 1: "过载"}, "normal_value": 0}
    },
    # BMS状态 (type=2)
    "bms": {
        "nowBatteryState": {"index": 0, "desc": "当前电池状态", "values": {0: "开路", 1: "充电", 2: "放电", 3: "搁置"}, "normal_value": None},
        "nowSystemState": {"index": 1, "desc": "当前系统状态", "values": {0: "初始", 1: "自检", 2: "上电", 3: "就绪", 4: "禁充", 5: "禁放", 6: "禁止充放", 7: "故障", 8: "故障恢复", 9: "强制控制测试模式", 10: "维护模式"}, "normal_value": None},
        "faultGrade": {"index": 2, "desc": "故障汇总等级", "values": {0: "正常", 1: "轻度告警", 2: "中度告警", 3: "严重告警"}, "normal_value": 0}
    },
    # 消防状态 (type=3)
    "fire": {
        "fireSolenoidValveControlOutput": {"bit": 0, "desc": "消防电磁阀控制输出", "values": {0: "正常", 1: "动作"}, "normal_value": 0},
        "fourInOneSensorOutput": {"bit": 1, "desc": "四合一传感器输出", "values": {0: "正常", 1: "动作"}, "normal_value": 0},
        "smokeSensorRunningStatus": {"bit": 2, "desc": "烟雾传感器运行状态", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
        "vocSensorRunningStatus": {"bit": 3, "desc": "VOC传感器运行状态", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
        "coSensorRunningStatus": {"bit": 4, "desc": "CO传感器运行状态", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
        "temperatureSensorRunningStatus": {"bit": 5, "desc": "温度传感器运行状态", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
        "smokeSensorAlarmStatus": {"bit": 6, "desc": "烟雾传感器告警状态", "values": {0: "正常", 1: "告警"}, "normal_value": 0},
        "vocSensorAlarmStatus": {"bit": 7, "desc": "VOC传感器告警状态", "values": {0: "正常", 1: "告警"}, "normal_value": 0},
        "coSensorAlarmStatus": {"bit": 8, "desc": "CO传感器告警状态", "values": {0: "正常", 1: "告警"}, "normal_value": 0},
        "temperatureSensorAlarmStatus": {"bit": 9, "desc": "温度传感器告警状态", "values": {0: "正常", 1: "告警"}, "normal_value": 0},
        "waterLoggingSensorAlarmStatus": {"bit": 10, "desc": "水浸传感器告警状态", "values": {0: "正常", 1: "告警"}, "normal_value": 0}
    }
}

# 类型映射
TYPE_MAPPING = {
    0: "system",
    1: "pcs",
    2: "bms",
    3: "fire",
    4: "other",
    5: "other",
    6: "other",
    7: "other",
    8: "other"
}

# 数据库配置
DB_CONFIG = {
    "db_file": "mqtt_records.db",
    "table_name": "device_records"
}

class DEVICE:
    DEVICE_ID = "FZAUS0000001"
    DEVICE_MODULE = "1"