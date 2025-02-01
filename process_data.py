import mysql.connector

# 連接 MySQL 數據庫
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123123",  # 替換為你的 MySQL 密碼
    database="my_database"
)
cursor = conn.cursor()

# 查詢數據
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# 打印數據
print("原始數據：")
for row in rows:
    print(row)

# 數據處理（例如過濾年齡大於 30 的用戶）
filtered_data = [row for row in rows if row[3] > 30]
print("\n過濾後的數據：")
for row in filtered_data:
    print(row)

# 關閉連接
cursor.close()
conn.close()