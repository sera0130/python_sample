
# 複合主キーのリスト
key_list = [
    {"pk1": 1, "pk2": 3, "pk3": 7},
    {"pk1": 1, "pk2": 3, "pk3": 8},
    {"pk1": 1, "pk2": 3, "pk3": 9},
]


# Pythonリスト → UNION ALL 形式に変換
# union_selects = " UNION ALL ".join(
#     f"SELECT {item['pk1']} AS pk1, {item['pk2']} AS pk2, {item['pk3']} AS pk3"
#     for item in key_list
# )
union_selects = " UNION ALL ".join(
    [
        f"SELECT {item['pk1']} AS pk1, "
        f"{item['pk2']} AS pk2, "
        f"{item['pk3']} AS pk3"
        for item in key_list
    ]
)

print(f"union_selects:{union_selects}")
