import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from the_modules.mendeley_client import get_authorization_url, exchange_code_for_token
import json

# Step 1: Print the authorization URL
print("\n=== Mendeley OAuth Setup ===")
auth_url = get_authorization_url()
print("1. Open this URL in your browser:")
print(auth_url)

# Step 2: Paste the code returned in the redirected URL
code = input("\n2. After authorizing, paste the 'code' from the URL here: ")

# Step 3: Exchange the code for a token
try:
    token_data = exchange_code_for_token(code)
    token_path = Path("secrets/mendeley_token.json")
    token_path.parent.mkdir(exist_ok=True)
    with open(token_path, "w") as f:
        json.dump(token_data, f, indent=2)
    print("\n✅ Access + Refresh tokens saved to secrets/mendeley_token.json")
except Exception as e:
    print("❌ Failed to exchange token:", e)
