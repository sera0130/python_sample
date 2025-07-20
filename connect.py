import mysql.connector

# MySQLへの接続設定
conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',   # ←ここは設定したものに置き換えてください
    database='mysql'    # ←接続するデータベース名
)

# カーソルを取得してSELECT文を実行
cursor = conn.cursor()
cursor.execute('SELECT * FROM db')  # ←テーブル名も適宜変更

# 結果を取得してコンソール出力
# for row in cursor.fetchall():
#     print(row)
# columns = [desc[0] for desc in cursor.description]
columns = ['Host', 'Db', 'User']
print(columns)

rows = cursor.fetchall()
dict_rows = [dict(zip(columns, row)) for row in rows]

dictRet = []

for record in dict_rows:
    print(record)
    dictRet.append(dict(record))

print(f"dictRet:{dictRet}")

# 後始末
cursor.close()
conn.close()