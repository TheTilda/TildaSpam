import asyncio
from pyrogram import Client
from config import *
import random

async def main():
    id_file = str(random.randint(111111111,999999999999999999))
    async with Client(id_file, api_id, api_hash) as app:
        await app.send_document("me", f"{id_file}.session")
    
asyncio.run(main())