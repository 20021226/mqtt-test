import sqlite3
import os
import time
from typing import Dict, Any, List
from config import DB_CONFIG

def init_database() -> sqlite3.Connection:
    """
    初始化SQLite数据库，如果不存在则创建
    
    :return: 数据库连接对象
    """
    # 检查数据库文件是否存在
    db_exists = os.path.exists(DB_CONFIG["db_file"])
    
    # 创建数据库连接
    conn = sqlite3.connect(DB_CONFIG["db_file"])
    
    # 如果数据库不存在，创建表
    if not db_exists:
        create_tables(conn)
    
    return conn

def create_tables(conn: sqlite3.Connection) -> None:
    """
    创建数据库表
    
    :param conn: 数据库连接对象
    """
    cursor = conn.cursor()
    
    # 创建记录表
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {DB_CONFIG["table_name"]} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp INTEGER NOT NULL,
        code TEXT NOT NULL,
        value INTEGER NOT NULL,
        description TEXT NOT NULL,
        is_normal BOOLEAN NOT NULL,
        type TEXT NOT NULL,
        module_number INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # 提交事务
    conn.commit()

def save_records(conn: sqlite3.Connection, records: List[Dict[str, Any]], timestamp: int) -> None:
    """
    保存记录到数据库
    
    :param conn: 数据库连接对象
    :param records: 记录列表
    :param timestamp: 时间戳
    """
    if not records:
        return
    
    cursor = conn.cursor()
    
    # 准备SQL语句
    sql = f'''
    INSERT INTO {DB_CONFIG["table_name"]} 
    (timestamp, code, value, description, is_normal, type, module_number)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    '''
    
    # 准备数据
    data = [
        (timestamp, record["code"], record["value"], record["desc"], 
         1 if record["normal"] else 0, record["type"], record["module_number"])
        for record in records
    ]
    
    # 执行批量插入
    cursor.executemany(sql, data)
    
    # 提交事务
    conn.commit()
    
    print(f"已保存 {len(records)} 条记录到数据库")

def query_records(limit: int = 10, type_filter: str = None, normal_filter: bool = None, module_number: int = None) -> List[tuple]:
    """
    查询记录
    
    :param limit: 限制返回的记录数量
    :param type_filter: 按类型过滤 (system, pcs, bms, fire, other)
    :param normal_filter: 按正常状态过滤 (True表示正常, False表示异常)
    :param module_number: 按模块编号过滤
    :return: 记录列表
    """
    conn = init_database()
    cursor = conn.cursor()
    
    # 构建查询条件
    conditions = []
    params = []
    
    if type_filter:
        conditions.append("type = ?")
        params.append(type_filter)
    
    if normal_filter is not None:
        conditions.append("is_normal = ?")
        params.append(1 if normal_filter else 0)
    
    if module_number is not None:
        conditions.append("module_number = ?")
        params.append(module_number)
    
    # 构建SQL查询
    sql = f"""
    SELECT id, timestamp, code, value, description, is_normal, type, module_number, created_at 
    FROM {DB_CONFIG['table_name']} 
    """
    
    if conditions:
        sql += "WHERE " + " AND ".join(conditions)
    
    sql += " ORDER BY id DESC LIMIT ?"
    params.append(limit)
    
    # 执行查询
    cursor.execute(sql, tuple(params))
    records = cursor.fetchall()
    
    conn.close()
    return records

def display_records(records: List[tuple]) -> None:
    """
    显示记录
    
    :param records: 记录列表
    """
    if records:
        print(f"查询到 {len(records)} 条记录:")
        for record in records:
            print(f"ID: {record[0]}")
            print(f"时间戳: {record[1]}")
            print(f"代码: {record[2]}")
            print(f"值: {record[3]}")
            print(f"描述: {record[4]}")
            print(f"是否正常: {'是' if record[5] else '否'}")
            print(f"类型: {record[6]}")
            print(f"模块编号: {record[7]}")
            print(f"创建时间: {record[8]}")
            print("---")
    else:
        print("没有找到符合条件的记录")

def get_db_stats() -> Dict[str, Any]:
    """
    获取数据库统计信息
    
    :return: 统计信息字典
    """
    conn = init_database()
    cursor = conn.cursor()
    
    # 获取总记录数
    cursor.execute(f"SELECT COUNT(*) FROM {DB_CONFIG['table_name']}")
    total_count = cursor.fetchone()[0]
    
    # 获取各类型记录数
    cursor.execute(f"SELECT type, COUNT(*) FROM {DB_CONFIG['table_name']} GROUP BY type")
    type_stats = cursor.fetchall()
    
    # 获取正常/异常记录数
    cursor.execute(f"SELECT is_normal, COUNT(*) FROM {DB_CONFIG['table_name']} GROUP BY is_normal")
    normal_stats = {row[0]: row[1] for row in cursor.fetchall()}
    normal_count = normal_stats.get(1, 0)
    abnormal_count = normal_stats.get(0, 0)
    
    # 获取最早和最新记录时间
    cursor.execute(f"SELECT MIN(created_at), MAX(created_at) FROM {DB_CONFIG['table_name']}")
    time_stats = cursor.fetchone()
    
    conn.close()
    
    # 返回统计信息
    return {
        "total_count": total_count,
        "normal_count": normal_count,
        "abnormal_count": abnormal_count,
        "type_stats": type_stats,
        "earliest_time": time_stats[0] if time_stats else None,
        "latest_time": time_stats[1] if time_stats else None
    }

def display_db_stats(stats: Dict[str, Any]) -> None:
    """
    显示数据库统计信息
    
    :param stats: 统计信息字典
    """
    total_count = stats["total_count"]
    normal_count = stats["normal_count"]
    abnormal_count = stats["abnormal_count"]
    type_stats = stats["type_stats"]
    earliest_time = stats["earliest_time"]
    latest_time = stats["latest_time"]
    
    # 显示统计信息
    print("数据库统计信息:")
    print(f"总记录数: {total_count}")
    print(f"正常记录数: {normal_count} ({normal_count/total_count*100:.1f}% 如果有记录)" if total_count > 0 else "正常记录数: 0 (0.0%)")
    print(f"异常记录数: {abnormal_count} ({abnormal_count/total_count*100:.1f}% 如果有记录)" if total_count > 0 else "异常记录数: 0 (0.0%)")
    
    print("\n各类型记录数:")
    for type_name, count in type_stats:
        print(f"  {type_name}: {count} ({count/total_count*100:.1f}% 如果有记录)" if total_count > 0 else f"  {type_name}: 0 (0.0%)")
    
    if earliest_time and latest_time:
        print(f"\n最早记录时间: {earliest_time}")
        print(f"最新记录时间: {latest_time}")

def clear_database() -> int:
    """
    清空数据库中的所有记录
    
    :return: 清空的记录数量
    """
    conn = init_database()
    cursor = conn.cursor()
    
    # 获取当前记录数
    cursor.execute(f"SELECT COUNT(*) FROM {DB_CONFIG['table_name']}")
    count = cursor.fetchone()[0]
    
    # 清空表
    cursor.execute(f"DELETE FROM {DB_CONFIG['table_name']}")
    conn.commit()
    
    conn.close()
    return count