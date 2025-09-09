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