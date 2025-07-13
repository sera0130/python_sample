from msal import ConfidentialClientApplication

# --- 変数の設定 ---
client_id = ''
client_secret = ''
tenant_id = ''
authority = f'https://login.microsoftonline.com/{tenant_id}'
scope = ['https://management.azure.com/.default']  # アクセス先に応じて変更

# --- MSAL アプリの作成 ---
app = ConfidentialClientApplication(
    client_id,
    authority=authority,
    client_credential=client_secret
)

# --- トークン取得 ---
result = app.acquire_token_for_client(scopes=scope)

if "access_token" in result:
    print("✅ Access Token:", result['access_token'])
else:
    print("❌ エラー:", result.get("error_description"))