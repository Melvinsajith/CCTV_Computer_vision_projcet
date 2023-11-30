from telethon import TelegramClient
import asyncio

## Run the following 2 lines if using Google Colab
import nest_asyncio
nest_asyncio.apply()

api_id='API_ID'
api_hash='API_HASH'
session_name= 'session1'
## must be your channel or have authorization to post
channel_invite_link = 't.me/AICats_Prompt' 


async def func():
    entity = await client.get_entity(channel_invite_link)
    # Send an image follow by a text.
    await client.send_file(entity, '/file/to/media.jpeg') 
    await client.send_message(entity=entity, message="Your text") 

# connection
async with TelegramClient(session_name, api_id, api_hash) as client:
    client.loop.run_until_complete(func())