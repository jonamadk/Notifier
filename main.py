from telethon import TelegramClient, events
from twilio.rest import Client
from credentials import *
import pygame


from datetime import datetime

now = datetime.now()
current_time = now.strftime("%I:%M %p")


pygame.init()

client = TelegramClient("my-session",API_ID, API_HASH)
print("Service Started")

@client.on(events.NewMessage(chats=CHANNEL_USERNAME))
async def  my_event_handler(event):
    """ Checks if there is slot message related to 2023

    Args:
        event (class): takes the chats object description
    """    
    latest_message = event.message.text
    print(f'update:{latest_message,current_time}')
    if "2023" in latest_message:
        pygame.mixer.music.load('alarm-1.mp3')
        pygame.mixer.music.play()
        #Uncomment below lines if you want to send the source message to any other channel to convery the message
        
        # for i in range(0,5):
        #     await client.send_message(1744031085, "DATE ALERT\t:\t"+latest_message)
        print("Slot opening Message:\t", latest_message)
        twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = twilio_client.messages.create(
        from_= FROM,
        body='EMERGENCY:  2023 KO  VISA DATE  KHULYO: Source'+ latest_message,
        to= TO
        )  

   
with client:
    client.run_until_disconnected()
    
    
    
    


