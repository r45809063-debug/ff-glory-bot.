import requests
import time
import random
import urllib3

# Ye line SSL warnings ko hide karne ke liye hai
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

USER_ID = "4631027154"
PASSWORD = "7A14AE50087AC2AA7EE80588458CBC931622F4A92307DC9DBB3FC47925166125"
REGION = "IND"

def start_glory_machine():
    print(f"--- Cloud Bot Active: ID {USER_ID} ---")
    url = "https://auth.ind.freefiremobile.com/api/v1/login/guest"
    
    headers = {
        "User-Agent": "FreeFire/2.103.1 (Android 11)",
        "Content-Type": "application/json"
    }
    
    data = {"account": USER_ID, "password": PASSWORD, "region": REGION}
    
    try:
        # Dhyaan se dekho, yahan 'verify=False' add kiya hai
        r = requests.post(url, json=data, headers=headers, timeout=20, verify=False)
        
        if r.status_code == 200:
            token = r.json().get("access_token")
            print(f"[SUCCESS] Login Done! Token: {token[:10]}...")
            
            # Matchmaking Start
            match_headers = {"Authorization": f"Bearer {token}"}
            print("[MATCH] Matchmaking Shuru...")
            requests.post("https://client.ind.freefiremobile.com/api/v1/match/start", 
                          headers=match_headers, json={"mode": 10}, verify=False, timeout=15)
            
            time.sleep(10)
            print("[EXIT] Match Leave! Glory added.")
            requests.post("https://client.ind.freefiremobile.com/api/v1/match/leave", 
                          headers=match_headers, verify=False, timeout=10)
        else:
            print(f"[FAILED] Garena Response: {r.status_code}")
            print(r.text)

    except Exception as e:
        print(f"[ERROR] Connection Failed: {e}")

if __name__ == "__main__":
    start_glory_machine()
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
