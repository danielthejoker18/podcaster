import os
try:
    import requests
except ImportError as e:
    raise SystemExit(
        "Missing 'requests' library. Install it with 'pip install requests'."
    ) from e

TOKEN = os.environ.get("CF_API_TOKEN")
ACCOUNT_ID = os.environ.get("CF_ACCOUNT_ID")

if not TOKEN:
    raise SystemExit("CF_API_TOKEN environment variable not set")
if not ACCOUNT_ID:
    raise SystemExit("CF_ACCOUNT_ID environment variable not set")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

try:
    resp = requests.get("https://api.cloudflare.com/client/v4/accounts", headers=headers, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    account_ids = [acc.get("id") for acc in data.get("result", [])]
    if ACCOUNT_ID in account_ids:
        print("Credentials are valid and have access to account", ACCOUNT_ID)
    else:
        print("Credentials valid but account ID not found")
except Exception as e:
    print("Error communicating with Cloudflare:", e)
