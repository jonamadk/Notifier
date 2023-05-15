import asyncio
import threading
from flask import Flask
from telethon import TelegramClient, events
from twilio.rest import Client
from credentials import *
import logging



app = Flask(__name__)

@app.route('/start')
def start():
    """ flask app of the algorithm

    Returns:
        _type_: _description_
    """    
    return 'Service started'

def run_telegram_listener():
    async def telegram_listener():
        client = TelegramClient('async-message_session', API_ID, API_HASH)
        await client.start()

        @client.on(events.NewMessage(chats=CHANNEL_USERNAME))
        async def my_event_handler(event):
            """ Checks if there is slot message related to 2023

            Args:
                event (class): takes the chats object description
            """
            latest_message = event.message.text
            print(f'update:{latest_message}')

            if "2023" in latest_message:
                print("Slot opening Message:\t", latest_message)
                twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
                message = twilio_client.messages.create(
                    from_=FROM,
                    body='EMERGENCY:  2023 KO  VISA DATE  KHULYO: Source' + latest_message,
                    to=TO
                )

        await client.run_until_disconnected()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(telegram_listener())

if __name__ == '__main__':
    telegram_thread = threading.Thread(target=run_telegram_listener, daemon=True)
    telegram_thread.start()

    app.run(debug=True)
