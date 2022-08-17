from datetime import datetime
import requests
import asyncio
import json
import requests
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from config import ConfigClass
import emoji
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

config = ConfigClass()

print("Starting deployment...")

client = TelegramClient(StringSession(config.session_string),config.api_id,config.api_hash)

def remove_emoji(text):
    # return emoji.get_emoji_regexp().sub(u'', text)
    return emoji.replace_emoji(text, replace='')


async def send_message(message):
    await client.send_message(config.to_chat, message, link_preview = False)
    
async def send_request(payload):
    r = requests.post(config.post_url, data=payload)
    
    
@client.on(events.NewMessage) # all incoming messages
# @client.on(events.NewMessage(outgoing=False)) # all incoming messages
async def my_event_handler(event):  
    newMessage = event.message.message # this is only a telegram message content, its what u see on telegram 
    FullMessage = event.message # this is full message event, with technical things undergoingm like some True, False, etc, and with buttons if any.
    
    newMessage = newMessage.lower()
    if config.remove_emoji:
        newMessage = remove_emoji(newMessage)

   
    if event.message.sender_id in config.from_chats and not config.filter_string in newMessage:
        print("There is No Required Key Word")

    elif event.message.sender_id in config.from_chats and config.filter_string in newMessage:
        newMessage = newMessage.replace(config.filter_string, config.filter_string_replace_to)
        dictionary ={
        "passphrase": config.passphrase,
        "forwarded_to": config.to_chat,
        "message": newMessage, 
        }
        json_object = json.dumps(dictionary, indent = 4)  
        await client.send_message(config.to_chat, newMessage, link_preview = False)
        print('Message Forwarded (', config.to_chat, '):' , newMessage)
        
        if config.webhook_request:
            await asyncio.gather(send_request(json_object))
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S") 
        
    else:
        print('No Active Redirection For This Message - SENDER ID:', event.message.sender_id, 'message:', newMessage)

print("Bot has been deployed.")
with client:
    client.run_until_disconnected()

