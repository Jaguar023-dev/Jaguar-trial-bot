from pywhatsapp import Client
client = Client()
client.login()
from pywhatsapp import Client
from datetime import datetime
client = Client()
client.login()
@client.on_message()
def reply(msg):
    if msg.body.lower() == 'hello':
        msg.reply('Hello, how are you?')
    elif msg.body.lower() == 'hi':
        msg.reply('Hi, how are you?')
@client.on_message()
def reply(msg):
    if msg.body.lower() == 'hello':
        msg.reply('Hello, how are you?')
    elif msg.body.lower() == 'hi':
        msg.reply('Hi, how are you?')
    elif msg.body.lower() == 'image':
        msg.reply('Here is an image', media='https://picsum.photos/200/300')
    elif msg.body.lower() == 'video':
        msg.reply('Here is a video', media='http://techslides.com/demos/sample-videos/small.mp4')
    else:
        msg.reply('Hello '+msg.sender.push_name+', how can I help you?')
from PIL import Image
from pywhatsapp import Client
from datetime import datetime
import requests
from io import BytesIO
client = Client()
client.login()
@client.on_message()
def reply(msg):
    if msg.body.lower() == 'hello':
        msg.reply('Hello, how are you?')
    elif msg.body.lower() == 'hi':
        msg.reply('Hi, how are you?')
    elif msg.body.lower() == 'image':
        msg.reply('Here is an image', media='https://picsum.photos/200/300')
    elif msg.body.lower() == 'video':
        msg.reply('Here is a video', media='http://techslides.com/demos/sample-videos/small.mp4')
    elif msg.body.lower().startswith('stick'):
        if len(msg.body.split()) > 1:
            if msg.body.split()[1].startswith('http'):
                response = requests.get(msg.body.split()[1])
                img = Image.open(BytesIO(response.content))
                img = img.convert("RGBA")
                img.save('sticker.png')
                msg.reply(media='sticker.png')
            elif msg.body.lower().split()[1] == 'text':
                if len(msg.body.split()) > 2:
                    text = msg.body.split()[2]
                    img = Image.new('RGB', (200, 200), (255, 255, 255))
                    d = Image.Draw(img)
                    d.text((10,10), text, fill=(0,0,0))
                    img.save('sticker.png')
                    msg.reply(media='sticker.png')
            else:
                msg.reply('Invalid sticker command')
        else:
            if msg.media:
                msg.download_media()
                img = Image.open(msg.media)
                img = img.convert("RGBA")
                img.save('sticker.png')
                msg.reply(media='sticker.png')
            else:
                msg.reply('Send an image or URL with stick command')
    else:
        msg.reply('Hello '+msg.sender.push_name+', how can I help you?')
@client.on_message()
def reply(msg):
    #previous code here...
    elif msg.body.lower().startswith('welcome'):
        if msg.is_group:
            msg.reply('Welcome to '+msg.chat.name+' group!')
    elif msg.body.lower().startswith('remove'):
        if msg.is_group:
            if len(msg.body.split()) > 1:
                number = msg.body.split()[1]
                client.remove_participant(msg.chat.id, number)
            else:
                msg.reply('Invalid remove command')
    elif msg.body.lower().startswith('mute'):
        if msg.is_group:
            client.mute_chat(msg.chat.id)
            msg.reply('Group muted')
    elif msg.body.lower().startswith('unmute'):
        if msg.is_group:
            client.unmute_chat(msg.chat.id)
            msg.reply('Group unmuted')
    elif msg.body.lower().startswith('rules'):
        if msg.is_group:
            msg.reply('Group rules: 
1. Be respectful
2. No spam')
from pywhatsapp import Client, parse_message
@client.on_message()
def reply(msg):
    #previous code here...
    elif msg.body.lower() == '!help':
        msg.reply('Commands: 
!menu - main menu
!about - about us
!help - this menu')
    elif msg.body.lower() == '!menu':
        msg.reply('Main Menu: 
1. Auto reply 
2. Media support 
3. Personalized responses 
4. Sticker maker 
5. Group Management')
    elif msg.body.lower() == '!about':
        msg.reply('About us: 
This is a WhatsApp bot made by Kenyan Jaguar')
    elif msg.body.lower().startswith('!addcommand'):
        if len(msg.body.split()) > 2:
            command = msg.body.split()[1]
            response = msg.body.split()[2]
            #save command and response to database or file
            msg.reply('Command added')
        else:
            msg.reply('Invalid command')
    elif msg.body.lower().startswith('!commands'):
        #load commands from database or file and reply
        msg.reply('Custom commands: 
(list of commands)')
users = []
@client.on_message()
def reply(msg):
    #previous code here...
    elif msg.body.lower().startswith('!anon'):
        users.append(msg.sender.id)
        if len(users) > 1:
            user1 = users[0]
            user2 = users[1]
            users.clear()
            client.send_message(user1, 'You are now chatting with a random user')
            client.send_message(user2, 'You are now chatting with a random user')
            @client.on_message()
            def anon_reply(msg):
                if msg.sender.id == user1:
                    client.send_message(user2, msg.body)
                elif msg.sender.id == user2:
                    client.send_message(user1, msg.body)
    elif msg.body.lower().startswith('!anonbot'):
        client.send_message(msg.sender.id, 'You are now chatting with the bot anonymously')
        @client.on_message()
        def anon_reply(msg):
            if msg.sender.id == msg.sender.id:
                client.send_message(msg.sender.id, 'Your message: '+msg.body)