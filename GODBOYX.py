import asyncio
import os
try:
  from pyrogram import Client, idle
except:
  os.system("pip install pyrogram>=1.1.13")
  from pyrogram import Client, idle

import asyncio
from DYNAMIC import bot as GODBOYX
API_ID = 3249905
API_HASH = ec7d3e4024ae97115b59e22dd6b4697c
from telethon import events, custom, Button, TelegramClient
import time
from DYNAMIC import ALIVE_NAME, bot
token = os.environ.get("BOT_TOKEN", None)
xbot = TelegramClient("GODBOYX", API_ID, API_HASH).start(bot_token=token)
pbot = Client("GODBOYX", api_id=API_ID, api_hash=API_HASH, bot_token=token)
NAME = str(ALIVE_NAME) if ALIVE_NAME else "DYNAMIC USER"
PHOTO = os.environ.get("ALIVE_PHOTO", None)
GODBOYX = "[GODBOYX](https://t.me/GODBOYX)"
VERSION = "1.1.0"
ID = 1742906647
REPO = "[Dynamic-Userbot](https://github.com/TeamDynamic/Dynamic-Userbot)"
devs = 1742906647
MASTER = f"[{NAME}](tg://user?id={ID})"
GROUP = "[SUPPORT GROUP](https://t.me/DYNAMICUSERBOTSUPPORT)"
if __name__=="__main__":
  xbot.run_until_disconnected()

if __name__=="__main__":
  pbot.start()
  run()
