import requests
import time
import random

# --- Aapki Set Details ---
USER_ID = "4631027154"
PASSWORD = "7A14AE50087AC2AA7EE80588458CBC931622F4A92307DC9DBB3FC47925166125"
REGION = "IND"

def start_glory_machine():
    print(f"--- Cloud Bot Active: ID {USER_ID} ---")
    
    # Garena Login URL
    url = "https://auth.ind.freefiremobile.com/api/v1/login/guest"
    
    headers = {
        "User-Agent": "FreeFire/2.103.1 (Android 11; Z80; Build/RP1A.200720.011)",
        "Content-Type": "application/json",
        "X-GA-ID": str(random.randint(111111, 999999))
    }
    
    data = {
        "account": USER_ID, 
        "password": PASSWORD, 
        "region": REGION
    }
    
    try:
        # Login Request
        r = requests.post(url, json=data, headers=headers, timeout=20)
        
        if r.status_code == 200:
            token = r.json().get("access_token")
            print(f"[SUCCESS] ID Online Aa Gayi! Token: {token[:10]}...")
            
            # Matchmaking Start (Mode 10 = Lone Wolf)
            print("[MATCH] Matchmaking Request Sent...")
            match_headers = {"Authorization": f"Bearer {token}"}
            m = requests.post("https://client.ind.freefiremobile.com/api/v1/match/start", 
                              headers=match_headers, json={"mode": 10}, timeout=15)
            
            # Thoda wait karke leave karna (Glory ke liye)
            time.sleep(15)
            print("[LEAVE] Leaving Match... Glory Added to Guild!")
            requests.post("https://client.ind.freefiremobile.com/api/v1/match/leave", 
                          headers=match_headers, timeout=10)
            
        elif r.status_code == 401:
            print("[ERROR] Password/Token galat hai ya expire ho gaya!")
        else:
            print(f"[FAILED] Server Error: {r.status_code}")
            print(f"Response: {r.text}")

    except Exception as e:
        print(f"[CONNECTION ERROR] Garena ne block kiya ya internet nahi hai: {e}")

if __name__ == "__main__":
    start_glory_machine()
