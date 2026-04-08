import requests, time, urllib3

urllib3.disable_warnings()

def start():
    ID, PW = "4631027154", "7A14AE50087AC2AA7EE80588458CBC931622F4A92307DC9DBB3FC47925166125"
    print(f"Bot Active: {ID}")
    
    try:
        r = requests.post(
            "https://auth.ind.freefiremobile.com/api/v1/login",
            json={
                "account": ID,
                "password": PW,
                "region": "IND",
                "type": 1
            },
            verify=False,
            timeout=20
        )

        if r.status_code == 200:
            tk = r.json().get("access_token")
            h = {"Authorization": f"Bearer {tk}"}

            requests.post(
                "https://client.ind.freefiremobile.com/api/v1/match/start",
                json={"mode": 10},
                headers=h,
                verify=False
            )

            print("Match Started...")
            time.sleep(15)

            requests.post(
                "https://client.ind.freefiremobile.com/api/v1/match/leave",
                headers=h,
                verify=False
            )

            print("Match Left! Glory Added.")

        else:
            print(f"Garena Error: {r.status_code}")

    except Exception as e:
        print(f"Fail: {e}")


if __name__ == "__main__":
    start()
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
