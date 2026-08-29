import os
from telethon import TelegramClient
from telethon.sessions import StringSession

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session = os.environ["SESSION_STRING"]
bot_username = os.environ["BOT_USERNAME"]
command = os.environ["COMMAND"]

async def main():
    async with TelegramClient(StringSession(session), api_id, api_hash) as client:
        await client.send_message(bot_username, command)
        print(f"Đã gửi: {command}")

import asyncio
asyncio.run(main())
