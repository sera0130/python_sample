import mysql.connector

# 複合主キーのリスト
key_list = [
    {"pk1": 1, "pk2": 3, "pk3": 7},
    {"pk1": 1, "pk2": 3, "pk3": 8},
    {"pk1": 1, "pk2": 3, "pk3": 9},
]

# MySQL接続
conn = mysql.connector.connect(
    host='your-host',
    user='your-user',
    password='your-password',
    database='your-db'
)
cursor = conn.cursor()

# Pythonリスト → UNION ALL 形式に変換（改行ありで可読性向上）
union_selects = " UNION ALL ".join([
    f"SELECT {item['pk1']} AS pk1, {item['pk2']} AS pk2, {item['pk3']} AS pk3"
    for item in key_list
])

# DELETEクエリ：リストにない組み合わせを削除
query = f"""
    DELETE FROM A
    WHERE NOT EXISTS (
        SELECT 1
        FROM (
            {union_selects}
        ) AS v
        WHERE v.pk1 = A.pk1 AND v.pk2 = A.pk2 AND v.pk3 = A.pk3
    )
"""

# 実行
cursor.execute(query)
conn.commit()

print(f"{cursor.rowcount} rows deleted.")

cursor.close()
conn.close()