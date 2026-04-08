import requests
import time

# --- Details ---
USER_ID = "4631027154"
PASSWORD = "7A14AE50087AC2AA7EE80588458CBC931622F4A92307DC9DBB3FC47925166125" 

def start_glory():
    print(f"Cloud Bot: Matchmaking for {USER_ID}...")
    # Yahan hum wahi login request bhejenge
    # Agar ye fail bhi ho, toh GitHub ise baar-baar try karta rahega
    url = "https://auth.ind.freefiremobile.com/api/v1/login/guest"
    try:
        r = requests.post(url, json={"account": USER_ID, "password": PASSWORD}, timeout=10)
        print(f"Status: {r.status_code}")
    except:
        print("Connection error, retrying later...")

if __name__ == "__main__":
    start_glory()
