import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session = os.environ["SESSION_STRING"]
bot_username = os.environ["BOT_USERNAME"]
command = os.environ["COMMAND"]

MAX_RETRIES = 3
WAIT_SECONDS = 120

async def main():
    async with TelegramClient(StringSession(session), api_id, api_hash) as client:
        async with client.conversation(bot_username, timeout=30) as conv:
            for attempt in range(1, MAX_RETRIES + 1):
                await conv.send_message(command)
                reply_text = ""
                try:
                    reply = await conv.get_response()
                    reply_text = reply.raw_text or ""
                except Exception:
                    pass

                print(f"Lần {attempt}: {reply_text}")

                if "xu" in reply_text.lower():
                    print(f"Thành công: {command}")
                    return

                if attempt < MAX_RETRIES:
                    print(f"Chưa thành công, đợi {WAIT_SECONDS}s rồi thử lại...")
                    await asyncio.sleep(WAIT_SECONDS)
                else:
                    print("Đã thử tối đa số lần, dừng lại.")

asyncio.run(main())
