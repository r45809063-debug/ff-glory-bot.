import requests
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

USER_ID = "4631027154"
PASSWORD = "7A14AE50087AC2AA7EE80588458CBC931622F4A92307DC9DBB3FC47925166125"

def start_glory_machine():
    print(f"--- Cloud Bot Active: ID {USER_ID} ---")
    
    # Naya updated login link
    url = "https://auth.ind.freefiremobile.com/api/v1/login"
    
    headers = {
        "User-Agent": "FreeFire/1.103.1 (Android 11)",
        "Content-Type": "application/json",
        "x-ga-id": "999888777"
    }
    
    # Is baar hum thoda naya data format bhej rahe hain
    data = {
        "account": USER_ID, 
        "password": PASSWORD, 
        "region": "IND",
        "type": 1 # Type 1 aksar Guest login ke liye hota hai
    }
    
    try:
        r = requests.post(url, json=data, headers=headers, timeout=20, verify=False)
        
        if r.status_code == 200:
            token = r.json().get("access_token")
            print("[SUCCESS] Login Done! ID Online.")
            
            # Matchmaking Link
            match_url = "https://client.ind.freefiremobile.com/api/v1/match/start"
            m_headers = {"Authorization": f"Bearer {token}"}
            requests.post(match_url, headers=m_headers, json={"mode": 10}, verify=False)
            
            print("[MATCH] Matchmaking Shuru... 15 sec wait.")
            time.sleep(15)
            
            requests.post("https://client.ind.freefiremobile.com/api/v1/match/leave", headers=m_headers, verify=False)
            print("[EXIT] Match Leave! Glory Added.")
        else:
            print(f"[FAILED] Garena ne link reject kiya: {r.status_code}")
            # Agar abhi bhi 404 aaye, toh iska matlab link abhi aur secret hai
    except Exception as e:
        print(f"[ERROR] Connection Failed: {e}")

if __name__ == "__main__":
    start_glory_machine()
            requests.post("https://client.ind.freefiremobile.com/api/v1/match/leave", 
                          headers=match_headers, verify=False, timeout=10)
        else:
            print(f"[FAILED] Garena Error: {r.status_code}")
            print(r.text)
    except Exception as e:
        print(f"[ERROR] Connection Failed: {e}")

if __name__ == "__main__":
    start_glory_machine()
