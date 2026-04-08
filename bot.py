import requests
import time

USER_ID = "4631027154"
PASSWORD = "7A14AE50087AC2AA7EE80588458CBC931622F4A92307DC9DBB3FC47925166125"

def start_glory():
    url = "https://auth.ind.freefiremobile.com/api/v1/login/guest"
    
    # Ye headers Garena ko dhokha dene ke liye hain
    headers = {
        "User-Agent": "FreeFire/2.103.1 (Android 11; Realme 8i)",
        "Content-Type": "application/json",
        "X-GA-ID": "123456789"
    }
    
    data = {"account": USER_ID, "password": PASSWORD, "region": "IND"}
    
    try:
        r = requests.post(url, json=data, headers=headers, timeout=15)
        print(f"Server Response: {r.status_code}")
        if r.status_code == 200:
            print("ID Online Ho Gayi! Matchmaking Shuru...")
        else:
            print("Garena ne block kiya. Error:", r.text)
    except Exception as e:
        print("Connection Error. Garena server tak nahi pahuch pa rahe.")

if __name__ == "__main__":
    start_glory()
if __name__ == "__main__":
    start_glory()
