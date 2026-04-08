import requests, time, urllib3
urllib3.disable_warnings()

ID = "4631027154"
PW = "7A14AE50087AC2AA7EE80588458CBC931622F4A92307DC9DBB3FC47925166125"

def start():
    print(f"Bot Active: {ID}")
    url = "https://auth.ind.freefiremobile.com/api/v1/login"
    data = {"account": ID, "password": PW, "region": "IND", "type": 1}
    try:
        r = requests.post(url, json=data, verify=False, timeout=20)
        if r.status_code == 200:
            tk = r.json().get("access_token")
            print("Login Success!")
            h = {"Authorization": f"Bearer {tk}"}
            requests.post("https://client.ind.freefiremobile.com/api/v1/match/start", json={"mode": 10}, headers=h, verify=False)
            time.sleep(15)
            requests.post("https://client.ind.freefiremobile.com/api/v1/match/leave", headers=h, verify=False)
            print("Match Done, Glory Added!")
        else:
            print(f"Error: {r.status_code}")
    except Exception as e:
        print(f"Fail: {e}")

if __name__ == "__main__":
    start()
            print(f"[FAILED] Garena Error: {r.status_code}")
            print(r.text)
    except Exception as e:
        print(f"[ERROR] Connection Failed: {e}")

if __name__ == "__main__":
    start_glory_machine()
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
