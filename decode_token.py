import jwt
import json

def decode_azure_access_token(access_token: str) -> dict | None:
    """
    Azure (Microsoft Entra ID) のアクセストークンをPyJWTライブラリでデコードします。
    この関数は署名の検証を行いません。
    
    Args:
        access_token (str): デコードしたいAzureアクセストークン（JWT形式）。

    Returns:
        dict | None: デコードされたトークンのペイロード（クレーム）の辞書、
                     またはデコードに失敗した場合はNone。
    """
    try:
        # PyJWTを使ってアクセストークンをデコード
        # options={"verify_signature": False} を設定することで、
        # 署名の検証をスキップし、単にトークンの内容をJSONとして取得します。
        # これは、トークンの内容を検査するためのものであり、セキュリティ目的の検証ではありません。
        decoded_payload = jwt.decode(
            jwt=access_token,
            key="",  # 署名検証をしないので空の文字列でOK
            algorithms=["RS256", "RS384", "RS512", "ES256", "ES384", "ES512"], # 一般的なアルゴリズムを列挙
            options={"verify_signature": False}
        )
        return decoded_payload

    except jwt.exceptions.DecodeError as e:
        print(f"Error: アクセストークンのデコードに失敗しました。JWT形式が不正な可能性があります。詳細: {e}")
        return None
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")
        return None

# --- 使用例 ---
if __name__ == "__main__":
    # ここに取得した実際のAzureアクセストークンを貼り付けてください。
    # 例: Graph Explorerなどで取得できるものなど
    your_azure_access_token = "" # ... (省略せず完全なトークンを貼り付ける)

    if your_azure_access_token == "":
        print("エラー: アクセストークンが指定されていません。'your_azure_access_token' に実際のトークンを貼り付けてください。")
    else:
        decoded_data = decode_azure_access_token(your_azure_access_token)

        if decoded_data:
            print("--- Azure アクセストークン (デコード済みペイロード) ---")
            print(json.dumps(decoded_data, indent=4))
            
            # アクセストークンの代表的なクレーム（ペイロード内の情報）をいくつか表示
            print("\n--- 主要なクレーム情報 ---")
            print(f"発行者 (iss): {decoded_data.get('iss')}")
            print(f"対象者 (aud): {decoded_data.get('aud')}")
            print(f"スコープ (scp): {decoded_data.get('scp')}") # スペース区切り文字列の場合が多い
            print(f"有効期限 (exp): {decoded_data.get('exp')} (Unixタイムスタンプ)")
            print(f"ユーザーID (oid): {decoded_data.get('oid')}")
            print(f"テナントID (tid): {decoded_data.get('tid')}")
            print(f"ユーザー名 (upn/preferred_username): {decoded_data.get('upn') or decoded_data.get('preferred_username')}")
            
            # Unixタイムスタンプを人間が読める形式に変換する例
            if 'exp' in decoded_data:
                import datetime
                expiration_time = datetime.datetime.fromtimestamp(decoded_data['exp'])
                print(f"有効期限 (現地時間): {expiration_time}")
        else:
            print("アクセストークンのデコード処理が完了しましたが、データは取得できませんでした。")

