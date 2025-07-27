import mysql.connector

# 削除リスト
deleteList = [{"id": 1}, {"id": 2}, {"id": 3}]
id_list = [item["id"] for item in deleteList]

# 仮想テーブル用の UNION ALL 句を構築
values_clause = " UNION ALL ".join([f"SELECT {id} AS id" for id in id_list])

# 差分抽出クエリ（tableAに存在しないidを抽出）
# query = f"""
#     SELECT dl.id
#     FROM ({values_clause}) AS dl
#     LEFT JOIN tableA AS a ON dl.id = a.id
#     WHERE a.id IS NULL;
# """
query = f"{values_clause}"
print("query:", query)

# DB接続（mysql.connector）
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',       # ←適宜変更
    database='mysql'       # ←接続するDB名に変更
)

# クエリ実行
cursor = connection.cursor()
cursor.execute(query)
results = cursor.fetchall()

# 結果整形（タプル → リスト）
missing_ids = [row[0] for row in results]
print("Missing IDs:", missing_ids)

# 後処理
cursor.close()
connection.close()