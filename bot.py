import requests, time, urllib3
urllib3.disable_warnings()

# Aapka Data
ID = "4631027154"
PW = "7A14AE50087AC2AA7EE80588458CBC931622F4A92307DC9DBB3FC47925166125"

def boost_glory():
    url = "https://auth.ind.freefiremobile.com/api/v1/login"
    data = {"account": ID, "password": PW, "region": "IND", "type": 1}
    try:
        r = requests.post(url, json=data, verify=False, timeout=20)
        if r.status_code == 200:
            tk = r.json().get("access_token")
            h = {"Authorization": f"Bearer {tk}"}
            print(f"Login Success! Boosting Glory for {ID}...")
            
            # Loop jo 5 baar match start/leave karega ek hi run mein
            for i in range(5):
                requests.post("https://client.ind.freefiremobile.com/api/v1/match/start", json={"mode": 10}, headers=h, verify=False)
                time.sleep(2) # Fast matchmaking
                requests.post("https://client.ind.freefiremobile.com/api/v1/match/leave", headers=h, verify=False)
                print(f"Match {i+1} Finished.")
            
            print("Batch Done! Glory updated in Guild.")
        else:
            print(f"Login Failed: {r.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    boost_glory()
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
