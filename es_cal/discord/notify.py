import requests
import os
import json


def send_message(content, embeds=[]):
    try:
        payload = {"content": content, "embeds": embeds}
        DISCORD_WEBHOOK = os.environ.get("DISCORD_NOTIFICATION_WEBHOOK")
        if DISCORD_WEBHOOK is None:
            print("NO WEBHOOK AVAILABLE")
            return
        print("SEND DATA DAMN IT")
        r = requests.post(
            DISCORD_WEBHOOK,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"},
        )   
        data = r.json()
        print(data)
        return data
    except Exception as e:
        print(e)
