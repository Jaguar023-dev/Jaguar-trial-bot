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