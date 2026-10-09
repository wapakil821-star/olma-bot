from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio, os
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
session_str = os.environ.get("SESSION")
kanal = os.environ.get("KANAL")
xet = """🍎 سورى ئالما بار
كۆپ بولسا ياخشى باهادا ئالىمەن
ئالاقە: @username"""
async def main():
    async with TelegramClient(StringSession(session_str), api_id, api_hash) as client:
        await client.send_message(kanal, xet)
        print("Yollandi!")
asyncio.run(main())
