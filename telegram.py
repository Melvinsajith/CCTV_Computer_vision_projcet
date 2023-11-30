import os
import sys
from telethon.sync import TelegramClient, events

# import nest_asyncio
# nest_asyncio.apply()

session_name = "<session_name>"
api_id = '6110698173:AAF4lnl-ZcRQ5pKvlzGPIMJoYmxaAmgg0dY'
api_hash = "<api_hash>"


os.chdir(sys.path[0])

if f"{session_name}.session" in os.listdir():
    os.remove(f"{session_name}.session")

async with TelegramClient(session_name, api_id, api_hash) as client:
   client.send_message('me', 'Hello, myself!')
   print(client.download_profile_photo('me'))

   @client.on(events.NewMessage(pattern='(?i).*Hello'))
   async def handler(event):
      await event.reply('Hey!')

   client.run_until_disconnected()