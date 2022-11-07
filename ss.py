import os



os.system("pip install telethon")
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


ULTROID = r"""
╭━━┳━━━━┳━━━┳╮╱╱╭━━┳━━━╮
╰┫┣┫╭╮╭╮┃╭━╮┃┃╱╱╰┫┣┫╭━╮┃
╱┃┃╰╯┃┃╰┫┃╱┃┃┃╱╱╱┃┃┃┃╱┃┃
╱┃┃╱╱┃┃╱┃╰━╯┃┃╱╭╮┃┃┃╰━╯┃
╭┫┣╮╱┃┃╱┃╭━╮┃╰━╯┣┫┣┫╭━╮┃
╰━━╯╱╰╯╱╰╯╱╰┻━━━┻━━┻╯╱╰╯
"""

okvai = ("")
if okvai == "":
    print(ULTROID)
    print("Please go to my.telegram.org and get your API Id and API Hash to proceed.")
    APP_ID = int(input("Enter APP ID here: "))
    API_HASH = input("Enter API HASH here: ")

    with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
        print("Check Your Saved Massages")
        client.send_message(
            "me",
            f"SESSION:\n\n`{client.session.save()}`\n\nMade With Love By [𝙄𝙏𝘼𝙇𝙄𝘼](t.me/IT_S6)",
        )