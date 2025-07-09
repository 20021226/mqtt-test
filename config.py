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
    },
    # 空调故障 (type=4)
    "airConditioner": {
        "byte1": {
            "returnAirTempSensorFault": {"bit": 0, "desc": "回风温感故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "condensationTempSensorFault": {"bit": 1, "desc": "冷凝温感故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "acStartStopStatus": {"bit": 2, "desc": "空调启停状态", "values": {0: "运行", 1: "停机"}, "normal_value": 0},
            "humiditySensorFault": {"bit": 3, "desc": "湿度传感故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0}
        },
        "byte2": {
            "highPressureAlarm": {"bit": 2, "desc": "高压力告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "cabinetHighTempAlarm": {"bit": 4, "desc": "柜内高温告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "cabinetLowTempAlarm": {"bit": 5, "desc": "柜内低温告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0}
        },
        "byte3": {
            "externalInputAlarm": {"bit": 1, "desc": "外部输入告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "cabinetHighHumidityAlarm": {"bit": 5, "desc": "柜内高湿告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0}
        },
        "byte4": {
            "highPressureFrequencyAlarm": {"bit": 4, "desc": "高压力频率告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "condensationHighTempAlarm": {"bit": 6, "desc": "冷凝高温告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "refrigerantLeakAlarm": {"bit": 7, "desc": "制冷剂泄漏告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0}
        }
    },
    # BMS故障 (type=5)
    "bmsFaults": {
        "mildAlarms": {
            "mildPowerUndervoltage": {"bit": 0, "desc": "供电欠压轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildPowerOvervoltage": {"bit": 1, "desc": "供电过压轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildEnvironmentOvertemperature": {"bit": 2, "desc": "环境过温轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildGroupUndervoltage": {"bit": 3, "desc": "组端欠压轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildGroupOvervoltage": {"bit": 4, "desc": "组端过压轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildPackPoleOvertemperature": {"bit": 5, "desc": "PACK极柱过温轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildChargeOcp": {"bit": 6, "desc": "充电过流轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildDischargeOcp": {"bit": 7, "desc": "放电过流轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildInsulationLow": {"bit": 8, "desc": "绝缘过低轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildSocLow": {"bit": 9, "desc": "SOC过低轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildMonomerOvervoltage": {"bit": 10, "desc": "单体过压轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildMonomerUndervoltage": {"bit": 11, "desc": "单体欠压轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildMonomerDropoutvoltageExcessive": {"bit": 12, "desc": "单体压差过大轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildRechargeOvertemperature": {"bit": 13, "desc": "充电过温轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildRechargeUndertemperature": {"bit": 14, "desc": "充电欠温轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildDischargeOvertemperature": {"bit": 15, "desc": "放电过温轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildDischargeUndertemperature": {"bit": 16, "desc": "放电欠温轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildMonomerTemperatureDifferenceExcessive": {"bit": 17, "desc": "单体温差大轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildTemperatureFast": {"bit": 18, "desc": "温升过快轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildHighVoltageBoxPoleOvertemperature": {"bit": 19, "desc": "高压盒极柱过温轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildDcBiternalResistanceExcessive": {"bit": 20, "desc": "直流内阻过大轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildDcBiternalResistanceDifferenceExcessive": {"bit": 21, "desc": "直流内阻差异过大轻度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildJustRelayLargeCurrentOperationFrequency": {"bit": 25, "desc": "主正继电器大电流操作次数过多", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildLoseRelayLargeCurrentOperationFrequency": {"bit": 26, "desc": "主负继电器大电流操作次数过多", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildFanFault": {"bit": 27, "desc": "风扇故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "mildParamOutRange": {"bit": 28, "desc": "参数超出范围故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0}
        },
        "moderateAlarms": {
            "moderatePowerUndervoltage": {"bit": 0, "desc": "供电欠压中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderatePowerOvervoltage": {"bit": 1, "desc": "供电过压中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateEnvironmentOvertemperature": {"bit": 2, "desc": "环境过温中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateGroupUndervoltage": {"bit": 3, "desc": "组端欠压中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateGroupOvervoltage": {"bit": 4, "desc": "组端过压中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderatePackPoleOvertemperature": {"bit": 5, "desc": "PACK极柱过温中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateChargeOcp": {"bit": 6, "desc": "充电过流中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateDischargeOcp": {"bit": 7, "desc": "放电过流中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateInsulationLow": {"bit": 8, "desc": "绝缘过低中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateSocLow": {"bit": 9, "desc": "SOC过低中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateMonomerOvervoltage": {"bit": 10, "desc": "单体过压中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateMonomerUndervoltage": {"bit": 11, "desc": "单体欠压中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateMonomerDropoutvoltageExcessive": {"bit": 12, "desc": "单体压差过大中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateRechargeOvertemperature": {"bit": 13, "desc": "充电过温中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateRechargeUndertemperature": {"bit": 14, "desc": "充电欠温中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateDischargeOvertemperature": {"bit": 15, "desc": "放电过温中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateDischargeUndertemperature": {"bit": 16, "desc": "放电欠温中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateMonomerTemperatureDifferenceExcessive": {"bit": 17, "desc": "单体温差大中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateWarmFast": {"bit": 18, "desc": "温升过快中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateHighVoltageBoxPoleOvertemperature": {"bit": 19, "desc": "高压盒极柱过温中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateDcBiternalResistanceExcessive": {"bit": 20, "desc": "直流内阻过大中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "moderateDcBiternalResistanceDifferenceExcessive": {"bit": 21, "desc": "直流内阻差异过大中度告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0}
        },
        "seriousAlarms": {
            "seriousPowerUndervoltage": {"bit": 0, "desc": "供电欠压严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousPowerOvervoltage": {"bit": 1, "desc": "供电过压严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousEnvironmentOvertemperature": {"bit": 2, "desc": "环境过温严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousGroupUndervoltage": {"bit": 3, "desc": "组端欠压严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousGroupOvervoltage": {"bit": 4, "desc": "组端过压严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousPackPoleOvertemperature": {"bit": 5, "desc": "PACK极柱过温严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousChargeOcp": {"bit": 6, "desc": "充电过流严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousDischargeOcp": {"bit": 7, "desc": "放电过流严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousInsulationLow": {"bit": 8, "desc": "绝缘过低严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousSocLow": {"bit": 9, "desc": "SOC过低严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousMonomerOvervoltage": {"bit": 10, "desc": "单体过压严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousMonomerUndervoltage": {"bit": 11, "desc": "单体欠压严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousMonomerDropoutvoltageExcessive": {"bit": 12, "desc": "单体压差过大严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousRechargeOvertemperature": {"bit": 13, "desc": "充电过温严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousRechargeUndertemperature": {"bit": 14, "desc": "充电欠温严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousDischargeOvertemperature": {"bit": 15, "desc": "放电过温严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousDischargeUndertemperature": {"bit": 16, "desc": "放电欠温严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousMonomerTemperatureDifferenceExcessive": {"bit": 17, "desc": "单体温差大严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousWarmFast": {"bit": 18, "desc": "温升过快严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousHighVoltageBoxPoleOvertemperature": {"bit": 19, "desc": "高压盒极柱过温严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousDcBiternalResistanceExcessive": {"bit": 20, "desc": "直流内阻过大严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousDcBiternalResistanceDifferenceExcessive": {"bit": 21, "desc": "直流内阻差异过大严重告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousThermorunaway": {"bit": 23, "desc": "热失控", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousHallSensor": {"bit": 24, "desc": "霍尔传感器故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousHighVoltageCollect": {"bit": 25, "desc": "高压采集故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousSingleVoltageCollectBreakLine": {"bit": 26, "desc": "单体电压采集断线", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousTemperatureCollectBreakLine": {"bit": 27, "desc": "温度采集线断线", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousPrecharge": {"bit": 28, "desc": "预充故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "serious6815Communication": {"bit": 29, "desc": "6815通讯故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousPackLeak": {"bit": 30, "desc": "pack进水故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "seriousHVIL": {"bit": 31, "desc": "packHVIL故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0}
        },
        "faults": {
            "postiveOnError": {"bit": 0, "desc": "主正继电器闭合故障，无法闭合", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "negativeOnError": {"bit": 1, "desc": "主负继电器闭合故障，无法闭合", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "prepOnError": {"bit": 2, "desc": "预充继电器闭合故障，无法闭合", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "postiveOffError": {"bit": 3, "desc": "主正继电器断开故障，触点粘连", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "negativeOffError": {"bit": 4, "desc": "主负继电器断开故障，触点粘连", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "prepareOffError": {"bit": 5, "desc": "预充继电器断开故障，触点粘连", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "wireFuse": {"bit": 6, "desc": "主正保险丝故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "PRingEShort": {"bit": 7, "desc": "主正继电器线圈对电源短路故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "PRingNShort": {"bit": 8, "desc": "主正继电器线圈对地短路故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "PRingFuse": {"bit": 9, "desc": "主正继电器线圈开路故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "NRingEShort": {"bit": 10, "desc": "主负继电器线圈对电源短路故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "NRingNShort": {"bit": 11, "desc": "主负继电器线圈对地短路故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "NRingFuse": {"bit": 12, "desc": "主负继电器线圈开路故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "prepareRingEShort": {"bit": 13, "desc": "预充继电器线圈对电源短路故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "prepareRingNShort": {"bit": 14, "desc": "预充继电器线圈对地短路故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "prepareRingFuse": {"bit": 15, "desc": "预充继电器线圈开路故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0}
        }
    },
    # PCS故障 (type=6)
    "pcsFaults": {
        "1": {
            "fpgaAOvercurrent": {"bit": 0, "desc": "硬件故障-A相硬件过流", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 1},
            "fpgaBOvercurrent": {"bit": 1, "desc": "硬件故障-B相硬件过流", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 1},
            "fpgaCOvercurrent": {"bit": 2, "desc": "硬件故障-C相硬件过流", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 1},
            "fpgaNOvercurrent": {"bit": 3, "desc": "硬件故障-N相硬件过流", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 1},
            "reservedBit4": {"bit": 4, "desc": "保留", "values": {}, "normal_value": 0, "array_index": 1},
            "reservedBit5": {"bit": 5, "desc": "保留", "values": {}, "normal_value": 0, "array_index": 1},
            "fpgaUnitStraightPress": {"bit": 6, "desc": "单元直压故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 1},
            "reservedBit7": {"bit": 7, "desc": "保留", "values": {}, "normal_value": 0, "array_index": 1},
            "reservedBit8": {"bit": 8, "desc": "保留", "values": {}, "normal_value": 0, "array_index": 1},
            "fpgaSwitchPowerUndervoltage": {"bit": 9, "desc": "硬件故障-开关电源欠压", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 1},
            "fpgaAIgbt": {"bit": 10, "desc": "软件故障-A相IGBT故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 1},
            "fpgaBIgbt": {"bit": 11, "desc": "硬件故障-B相IGBT故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 1},
            "fpgaCIgbt": {"bit": 12, "desc": "硬件故障-C相IGBT故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 1},
            "fpgaNIgbt": {"bit": 13, "desc": "硬件故障-N相IGBT故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 1},
            "fpgaOverTemperature": {"bit": 14, "desc": "硬件故障-过温故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 1},
            "reservedBit15": {"bit": 15, "desc": "保留", "values": {}, "normal_value": 0, "array_index": 1}
        },
        "2": {
            "armAOcp": {"bit": 0, "desc": "软件故障-A相输出过流", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 2},
            "armAQb": {"bit": 1, "desc": "软件故障-A相输出速断", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 2},
            "armBOcp": {"bit": 2, "desc": "软件故障-B相输出过流", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 2},
            "armBQb": {"bit": 3, "desc": "软件故障-B相输出速断", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 2},
            "armCOcp": {"bit": 4, "desc": "软件故障-C相输出过流", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 2},
            "armCQb": {"bit": 5, "desc": "软件故障-C相输出速断", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 2},
            "armNOcp": {"bit": 6, "desc": "软件故障-N相输出过流", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 2},
            "armNQb": {"bit": 7, "desc": "软件故障-N相输出速断", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 2},
            "armAcOvervoltage": {"bit": 8, "desc": "软件故障-交流过压", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 2},
            "armAcUndervoltage": {"bit": 9, "desc": "软件故障-交流欠压", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 2},
            "armAcOverfrequency": {"bit": 10, "desc": "软件故障-交流过频", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 2},
            "armAcUnderfrequency": {"bit": 11, "desc": "软件故障-交流欠频", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 2},
            "armThduTransfinite": {"bit": 12, "desc": "软件故障-电压THDU超限", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 2},
            "armSystemOverload": {"bit": 13, "desc": "软件故障-系统缺相", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 2},
            "armSystemSequenceError": {"bit": 14, "desc": "软件故障-系统相序错误", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 2},
            "armDcReverse": {"bit": 15, "desc": "软件故障-直流极性反接", "values": {0: "正常", 1: "故障"}, "normal_value": 0, "array_index": 2}
        },
        "3": {
            "armDcLineOvervoltage": {"bit": 0, "desc": "软件故障-直流母线软件过压", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armDcLineUndervoltage": {"bit": 1, "desc": "软件故障-直流母线软件欠压", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armSystemOverfrequency": {"bit": 2, "desc": "软件故障-系统过频率", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armSystemUnderfrequency": {"bit": 3, "desc": "软件故障-系统欠频率", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armDcRechargeOcp": {"bit": 4, "desc": "软件故障-直流充电过流", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armDcDischargeOcp": {"bit": 5, "desc": "软件故障-直流放电过流", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armIsletProtect": {"bit": 6, "desc": "软件故障-孤岛保护", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "reservedBit7": {"bit": 7, "desc": "保留", "values": {}, "normal_value": 0},
            "armAcMainSwitchMerge": {"bit": 8, "desc": "软件故障-交流主接合闸故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armAcMainSwitchPart": {"bit": 9, "desc": "软件故障-交流主接分闸故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armAcSsSwitchMerge": {"bit": 10, "desc": "软件故障-交流软启合闸故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armAcSsSwitchPart": {"bit": 11, "desc": "软件故障-交流软启分闸故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armDcMainSwitchMerge": {"bit": 12, "desc": "软件故障-直流主接合闸故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armDcMainSwitchPart": {"bit": 13, "desc": "软件故障-直流主接分闸故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armDcSsSwitchMerge": {"bit": 14, "desc": "软件故障-直流软启合闸故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armDcSsSwitchPart": {"bit": 15, "desc": "软件故障-直流软启分闸故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0}
        },
        "4": {
            "armFerroelectricParamError": {"bit": 0, "desc": "软件故障-铁电参数存储错误", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armDcSsFail": {"bit": 1, "desc": "软件故障-直流软起失败", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "reservedBit2": {"bit": 2, "desc": "保留", "values": {}, "normal_value": 0},
            "reservedBit3": {"bit": 3, "desc": "保留", "values": {}, "normal_value": 0},
            "armStartDiscontent": {"bit": 4, "desc": "软件故障-起机条件不满足", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armRunSwitch": {"bit": 5, "desc": "软件故障-运行中开关故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armInverterStartTimeout": {"bit": 6, "desc": "软件故障-逆变启动超时", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armParamIssueError": {"bit": 7, "desc": "软件故障-参数下发设置错误", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armBmsCommunicate": {"bit": 8, "desc": "软件故障-BMS通讯故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armBmsTemperature": {"bit": 9, "desc": "软件故障-BMS温度异常", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armBmsJumpoff": {"bit": 10, "desc": "软件故障-BMS跳机", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armBmsBattery": {"bit": 11, "desc": "软件故障-BMS电池告警", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "armDcdcCommunicate": {"bit": 12, "desc": "软件故障-DCDC通讯故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "reservedBit13": {"bit": 13, "desc": "保留", "values": {}, "normal_value": 0},
            "armScramFusiblecore": {"bit": 14, "desc": "软件故障-急停或熔芯故障", "values": {0: "正常", 1: "故障"}, "normal_value": 0},
            "reservedBit15": {"bit": 15, "desc": "保留", "values": {}, "normal_value": 0}
        }
    },
    # DCDC故障 (type=7)
    "dcdcFaults": {
        "byte1": {
            "pv1InputOvercurrent": {"bit": 0, "desc": "PV1输入过流", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv2InputOvercurrent": {"bit": 1, "desc": "PV2输入过流", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv3InputOvercurrent": {"bit": 2, "desc": "PV3输入过流", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv4InputOvercurrent": {"bit": 3, "desc": "PV4输入过流", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv1InputOvervoltage": {"bit": 4, "desc": "PV1输入过压", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv2InputOvervoltage": {"bit": 5, "desc": "PV2输入过压", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv3InputOvervoltage": {"bit": 6, "desc": "PV3输入过压", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv4InputOvervoltage": {"bit": 7, "desc": "PV4输入过压", "values": {0: "正常", 1: "触发"}, "normal_value": 0}
        },
        "byte2": {
            "pv1InputUndervoltage": {"bit": 0, "desc": "PV1输入欠压", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv2InputUndervoltage": {"bit": 1, "desc": "PV2输入欠压", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv3InputUndervoltage": {"bit": 2, "desc": "PV3输入欠压", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv4InputUndervoltage": {"bit": 3, "desc": "PV4输入欠压", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv1ReverseConnection": {"bit": 4, "desc": "PV1反接", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv2ReverseConnection": {"bit": 5, "desc": "PV2反接", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv3ReverseConnection": {"bit": 6, "desc": "PV3反接", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv4ReverseConnection": {"bit": 7, "desc": "PV4反接", "values": {0: "正常", 1: "触发"}, "normal_value": 0}
        },
        "byte3": {
            "busOvervoltage": {"bit": 0, "desc": "母线过压", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "busUndervoltage": {"bit": 1, "desc": "母线欠压", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "highVoltageSideHardwareOvercurrent": {"bit": 2, "desc": "高压侧硬件过流", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "prechargeTimeout": {"bit": 3, "desc": "预充电超时", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "insulationImpedanceDetectionFailure": {"bit": 4, "desc": "绝缘阻抗检测失效", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "coolingFanFault": {"bit": 5, "desc": "散热风扇故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "lowVoltageSide1HardwareOvervoltage": {"bit": 6, "desc": "低压侧1硬件过压", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "lowVoltageSide2HardwareOvervoltage": {"bit": 7, "desc": "低压侧2硬件过压", "values": {0: "正常", 1: "触发"}, "normal_value": 0}
        },
        "byte4": {
            "lowVoltageSide3HardwareOvervoltage": {"bit": 0, "desc": "低压侧3硬件过压", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "lowVoltageSide4HardwareOvervoltage": {"bit": 1, "desc": "低压侧4硬件过压", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "highVoltageSideWaveLimitOverrun": {"bit": 2, "desc": "高压侧逐波限流超限", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "masterFault": {"bit": 3, "desc": "主机故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "slaveFault": {"bit": 4, "desc": "从机故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "masterSlaveCommVersionError": {"bit": 5, "desc": "主从通讯版本错误", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "emergencyStopFault": {"bit": 6, "desc": "紧急停机故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "otherFault": {"bit": 7, "desc": "其它故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0}
        },
        "byte5": {
            "highVoltageSideReverseConnection": {"bit": 3, "desc": "高压侧反接", "values": {0: "正常", 1: "触发"}, "normal_value": 0}
        },
        "byte7": {
            "lowVoltageSide1HardwareOvercurrent": {"bit": 0, "desc": "低压侧1硬件过流", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "lowVoltageSide2HardwareOvercurrent": {"bit": 1, "desc": "低压侧2硬件过流", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "lowVoltageSide3HardwareOvercurrent": {"bit": 2, "desc": "低压侧3硬件过流", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "lowVoltageSide4HardwareOvercurrent": {"bit": 3, "desc": "低压侧4硬件过流", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "auxiliaryPowerFault": {"bit": 4, "desc": "辅助电源故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "moduleOverTemperature": {"bit": 5, "desc": "模块过温", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "lowAmbientTemperature": {"bit": 6, "desc": "环境温度低", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "highVoltageSideHardwareOvercurrent": {"bit": 7, "desc": "高压侧硬件过流", "values": {0: "正常", 1: "触发"}, "normal_value": 0}
        },
        "byte8": {
            "busHardwareOvervoltage": {"bit": 0, "desc": "母线硬件过压", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "emsCommunicationFault": {"bit": 1, "desc": "EMS通讯故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "lowVoltageSide1WaveLimit": {"bit": 2, "desc": "低压侧1逐波限流", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "lowVoltageSide2WaveLimit": {"bit": 3, "desc": "低压侧2逐波限流", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "lowVoltageSide3WaveLimit": {"bit": 4, "desc": "低压侧3逐波限流", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "lowVoltageSide4WaveLimit": {"bit": 5, "desc": "低压侧4逐波限流", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "masterSlaveCommunicationFault": {"bit": 6, "desc": "主从通讯故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "highAmbientTemperature": {"bit": 7, "desc": "环境温度高", "values": {0: "正常", 1: "触发"}, "normal_value": 0}
        },
        "byte9": {
            "pv1ShortCircuit": {"bit": 0, "desc": "PV1短路", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv2ShortCircuit": {"bit": 1, "desc": "PV2短路", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv3ShortCircuit": {"bit": 2, "desc": "PV3短路", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "pv4ShortCircuit": {"bit": 3, "desc": "PV4短路", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
            "adZeroDriftExcessive": {"bit": 4, "desc": "AD零漂过大", "values": {0: "正常", 1: "触发"}, "normal_value": 0}
        }
    },
    # 液冷故障 (type=8)
    "liquidCoolingFaults": {
        "parameterError": {"number": 3, "desc": "参数错误故障（控制板）", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "inputPhaseSequenceFault": {"number": 4, "desc": "输入相序检测故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "threePhaseDetectionFault": {"number": 5, "desc": "三相检测缺相故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "overspeedProtection": {"number": 6, "desc": "超速保护", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "packReturnWaterTempSensorFault": {"number": 7, "desc": "Pack侧回水温度传感器故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "packOutletWaterTempSensorFault": {"number": 8, "desc": "Pack侧出水温度传感器故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "ambientTempSensorFault": {"number": 9, "desc": "外环境温度传感器故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "exhaustTempSensorFault": {"number": 11, "desc": "排气温度传感器故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "controllerMainBoardCommFault": {"number": 16, "desc": "485通讯故障（线控器与主控板）", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "mainDriveBoardCommFault": {"number": 17, "desc": "主板与驱动板通讯故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "packOutletWaterPressureSensorFault": {"number": 18, "desc": "Pack侧出水压力传感器故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "packInletWaterPressureSensorFault": {"number": 19, "desc": "Pack侧进水压力传感器故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "compressorOvercurrentProtection": {"number": 24, "desc": "压机电流过流保护", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "packCoolingOutletWaterTempLowProtection": {"number": 26, "desc": "Pack侧制冷出水温度过低保护", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "packOutletWaterTempHighProtection": {"number": 29, "desc": "Pack侧出水温度过高保护", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "exhaustTempHighProtection": {"number": 30, "desc": "排气温度过高保护", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "highPressureSensorFault": {"number": 32, "desc": "高压传感器故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "lowPressureSensorFault": {"number": 33, "desc": "低压传感器故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "highPressureProtection": {"number": 36, "desc": "高压压力保护", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "lowPressureProtection": {"number": 37, "desc": "低压压力保护", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "packWaterReplenishmentAlarm": {"number": 38, "desc": "Pack侧补水告警", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "liquidLevelSwitchAlarm": {"number": 39, "desc": "液位开关报警", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "outdoorDcFan1Fault": {"number": 41, "desc": "室外直流风机1故障/风机过载或者缺失", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "packOutletWaterPressureHighAlarm": {"number": 42, "desc": "Pack侧出水压力过高报警", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "driveModuleFault": {"number": 44, "desc": "驱动模块故障（FO)输出短路保护", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "dcBusVoltageFault": {"number": 46, "desc": "直流母线电压过高、过低保护、输入电压检测故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "driveModuleTempHighProtection": {"number": 47, "desc": "驱动模块温度过高保护停机/散热器温度检测/IPM温度检测故障/散热器过热/IPM模块过热", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "compressorStartAbnormal": {"number": 48, "desc": "压缩机启动异常(缺相、反转)、输出三相不平", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "compressorOutOfStepFault": {"number": 49, "desc": "压缩机失步故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "inverterSideHardwareOvercurrent": {"number": 50, "desc": "变频侧硬件瞬时过流输出过载保护", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "inverterSideInstantOvercurrent": {"number": 51, "desc": "变频侧瞬时过流检出输出过流保护", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "rectifierSideSoftwareOvercurrent": {"number": 52, "desc": "整流侧软件瞬时过流输入过流保护", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "rectifierSideHardwareOvercurrent": {"number": 53, "desc": "整流侧硬件瞬时过流母线电流检测故障、输入电流检测故障、输入短路保护", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "outdoorDcFan2Fault": {"number": 55, "desc": "室外直流风机2故障/风机过载或者缺失", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "packWaterPumpDriveFault": {"number": 65, "desc": "Pack侧水泵驱动故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "pcsWaterPumpDriveFault": {"number": 66, "desc": "Pcs侧水泵驱动故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "pcsReturnWaterTempSensorFault": {"number": 67, "desc": "Pcs侧回水温度传感器故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "pcsOutletWaterTempSensorFault": {"number": 68, "desc": "Pcs侧出水温度传感器故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "pcsOutletWaterPressureSensorFault": {"number": 69, "desc": "Pcs侧出水压力传感器故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "pcsInletWaterPressureSensorFault": {"number": 70, "desc": "Pcs侧进水压力传感器故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "pcsCoolingOutletWaterTempLowProtection": {"number": 71, "desc": "Pcs侧制冷出水温度过低保护", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "pcsOutletWaterTempHighProtection": {"number": 72, "desc": "Pcs侧出水温度过高保护", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "pcsWaterReplenishmentAlarm": {"number": 73, "desc": "Pcs侧补水告警", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "pcsOutletWaterPressureHighAlarm": {"number": 74, "desc": "Pcs侧出水压力过高报警", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "packGasPipeTempSensorFault": {"number": 75, "desc": "Pack侧气管温度传感器故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "packLiquidPipeTempSensorFault": {"number": 76, "desc": "Pack侧液管温度传感器故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "pcsGasPipeTempSensorFault": {"number": 77, "desc": "Pcs侧气管温度传感器故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0},
        "pcsLiquidPipeTempSensorFault": {"number": 78, "desc": "Pcs侧液管温度传感器故障", "values": {0: "正常", 1: "触发"}, "normal_value": 0}
    }
}

# 类型映射
TYPE_MAPPING = {
    0: "system",
    1: "pcs",
    2: "bms",
    3: "fire",
    4: "airConditioner",
    5: "bmsFaults",
    6: "pcsFaults",
    7: "dcdcFaults",
    8: "liquidCoolingFaults",
}

# 数据库配置
DB_CONFIG = {
    "db_file": "mqtt_records.db",
    "table_name": "device_records"
}

class DEVICE:
    DEVICE_ID = "FZAUS0000001"
    DEVICE_MODULE = "1"