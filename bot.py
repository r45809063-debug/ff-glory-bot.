import requests
import time

# --- Aapki Details ---
USER_ID = "4631027154"
PASSWORD = "7A14AE50087AC2AA7EE80588458CBC931622F4A92307DC9DBB3FC47925166125" # Yahan apna sahi password dalo
REGION = "IND"

def start_bot():
    print(f"--- Glory Bot Shuru: ID {USER_ID} ---")
    
    # 1. Server par Login Request
    login_url = "https://auth.ind.freefiremobile.com/api/v1/login/guest"
    try:
        r = requests.post(login_url, json={"account": USER_ID, "password": PASSWORD, "region": REGION}, timeout=15)
        if r.status_code == 200:
            token = r.json().get("access_token")
            print("[SUCCESS] Login Ho Gaya! Token Mil Gaya.")
            
            # 2. Matchmaking Signal (Lone Wolf ya Jo aapki script support kare)
            print("[MATCH] Matchmaking Shuru kar raha hu...")
            match_url = "https://client.ind.freefiremobile.com/api/v1/match/start"
            headers = {"Authorization": f"Bearer {token}"}
            requests.post(match_url, headers=headers, json={"mode": 10}, timeout=10)
            
            # 3. Wait aur phir Match Leave (Glory ke liye)
            time.sleep(10)
            print("[EXIT] Match Leave! Glory Guild mein add ho gayi.")
            leave_url = "https://client.ind.freefiremobile.com/api/v1/match/leave"
            requests.post(leave_url, headers=headers, timeout=10)
            
        else:
            print(f"[FAILED] Login Fail! Status Code: {r.status_code}")
    except Exception as e:
        print(f"[ERROR] Connection Issue: {e}")

if __name__ == "__main__":
    start_glory()
