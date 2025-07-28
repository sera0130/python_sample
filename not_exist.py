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

# Pythonリスト → UNION ALL 形式に変換
union_selects = " UNION ALL ".join(
    f"SELECT {item['pk1']} AS pk1, {item['pk2']} AS pk2, {item['pk3']} AS pk3"
    for item in key_list
)

# INSERTクエリ：存在しない組み合わせのみ挿入
query = f"""
    INSERT INTO A (pk1, pk2, pk3)
    SELECT v.pk1, v.pk2, v.pk3
    FROM (
        {union_selects}
    ) AS v
    LEFT JOIN A
    ON v.pk1 = A.pk1 AND v.pk2 = A.pk2 AND v.pk3 = A.pk3
    WHERE A.pk1 IS NULL
"""

# 実行
cursor.execute(query)
conn.commit()

print(f"{cursor.rowcount} rows inserted.")

cursor.close()
conn.close()