import requests, time, random, urllib3

# SSL Error fix karne ke liye
urllib3.disable_warnings()

# --- AAPKI DETAILS ---
USER_ID = "4631027154"
PASSWORD = "7A14AE50087AC2AA7EE80588458CBC931622F4A92307DC9DBB3FC47925166125"

def start_bot():
    print(f"Connecting to Garena for ID: {USER_ID}...")
    
    # Ye wahi APIs hain jo JamiulGaming wali script use karti hai
    login_url = "https://auth.ind.freefiremobile.com/api/v1/login"
    
    headers = {
        "User-Agent": "FreeFire/1.103.1 (Android 11; Build/RP1A.200720.011)",
        "Content-Type": "application/json",
        "X-GA-ID": str(random.randint(100000, 999999))
    }

    payload = {
        "account": USER_ID,
        "password": PASSWORD,
        "region": "IND",
        "type": 1
    }

    try:
        # 1. LOGIN
        r = requests.post(login_url, json=payload, headers=headers, verify=False, timeout=20)
        
        if r.status_code == 200:
            token = r.json().get("access_token")
            print("✅ [SUCCESS] ID Online Aa Gayi!")
            
            # 2. MATCHMAKING (Mode 10 = Lone Wolf for Glory)
            m_headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            print("🚀 [MATCH] Matchmaking Shuru...")
            requests.post("https://client.ind.freefiremobile.com/api/v1/match/start", 
                          json={"mode": 10}, headers=m_headers, verify=False)
            
            # 15 second wait taaki match lag jaye
            time.sleep(15)
            
            # 3. LEAVE MATCH
            print("🚪 [EXIT] Match Leaving for Glory...")
            requests.post("https://client.ind.freefiremobile.com/api/v1/match/leave", 
                          headers=m_headers, verify=False)
            print("✨ [DONE] Glory Added! Bot Sleeping...")
            
        else:
            print(f"❌ [FAILED] Garena ne reject kiya: {r.status_code}")
            print(f"Message: {r.text}")
            
    except Exception as e:
        print(f"⚠️ [ERROR] Connection Problem: {e}")

if __name__ == "__main__":
    start_bot()
            # Match start
            requests.post(
                "https://client.ind.freefiremobile.com/api/v1/match/start",
                json={"mode": 10},
                headers=match_headers,
                verify=False,
                timeout=15
            )

            print("Match Started...")
            time.sleep(15)

            # Match leave
            requests.post(
                "https://client.ind.freefiremobile.com/api/v1/match/leave",
                headers=match_headers,
                verify=False,
                timeout=10
            )

            print("Match Left! Glory Added.")

        else:
            print(f"Garena Error: {r.status_code}")
            print(r.text)

    except Exception as e:
        print(f"Fail: {e}")


if __name__ == "__main__":
    start()
            # Match start
            requests.post(
                "https://client.ind.freefiremobile.com/api/v1/match/start",
                json={"mode": 10},
                headers=h,
                verify=False,
                timeout=15
            )

            print("Match Started...")
            time.sleep(15)

            # Match leave
            requests.post(
                "https://client.ind.freefiremobile.com/api/v1/match/leave",
                headers=h,
                verify=False,
                timeout=10
            )

            print("Match Left! Glory Added.")

        else:
            print(f"Garena Error: {r.status_code}")
            print(r.text)

    except Exception as e:
        print(f"Fail: {e}")


if __name__ == "__main__":
    start()                          headers=match_headers, verify=False, timeout=10)
        else:
            print(f"[FAILED] Garena Error: {r.status_code}")
            print(r.text)
    except Exception as e:
        print(f"[ERROR] Connection Failed: {e}")

if __name__ == "__main__":
    start_glory_machine()
