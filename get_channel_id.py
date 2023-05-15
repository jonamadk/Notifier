from telethon import TelegramClient, events
from cred_config import *

client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(chats='https://t.me/+bLDNVuxY4E40YTRl'))
async def handler(event):
    
    """
    args: The link of channel.
    

    prints the Id of that very channel Id once msg is send in that very channel.
    """
    chat = await event.get_chat()
    channel_id = chat.id
    print(channel_id)

with client:
    client.run_until_disconnected()
