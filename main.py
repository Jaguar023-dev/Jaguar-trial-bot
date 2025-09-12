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
    if msg.body.lower().startswith('welcome'):
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
            msg.reply("Group rules: ") 
msg.reply("""1. No spam 
2. Be respectful""") 
from pywhatsapp import Client, parse_message
@client.on_message()
def reply(msg):
    #previous code here...
    if msg.body.lower() == '!help':
        msg.reply("""Commands: """)
print('!menu - main menu')
print('!about - about us')
msg.reply('!help - this menu')
if msg.body.lower() == '!menu':
        msg.reply('Main Menu:')
print('1. Auto reply')
print('2. Media support')
print('3. Personalized responses')
print('4. Sticker maker')
print('5. Group Management')
if msg.body.lower() == '!about':
    print('About us:')
print('This is a WhatsApp bot made by Kenyan Jaguar')
if msg.body.lower().startswith('!addcommand'):
        if len(msg.body.split()) > 2:
            command = msg.body.split()[1]
            response = msg.body.split()[2]
            #save command and response to database or file
            msg.reply('Command added')
        else:
            msg.reply('Invalid command')
if msg.body.lower().startswith('!commands'):
        #load commands from database or file and reply
        msg.reply("Custom commands")
print('list of commands')
users = []
@client.on_message()
def reply(msg):
    #previous code here...
    if msg.body.lower().startswith('!anon'):
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
@client.on_message()
def reply(msg):
    #previous code here...
    if msg.body.lower().startswith('!broadcast'):
        if len(msg.body.split()) > 1:
            message = msg.body.split()[1]
            for chat in client.get_chats():
                client.send_message(chat.id, message)
            msg.reply('Broadcast sent to all contacts')
    if msg.body.lower().startswith('!broadcast'):
        print('broadcast group')
        if len(msg.body.split()) > 2:
            group_name = msg.body.split()[1]
            message = msg.body.split()[2]
            for chat in client.get_chats():
                if chat.name == group_name:
                    client.send_message(chat.id, message)
            msg.reply('Broadcast sent to '+group_name)
import openai
openai.api_key = 'YOUR_API_KEY'
@client.on_message()
def reply(msg):
    #previous code here...
    if msg.body.lower().startswith('!ask'):
        prompt = msg.body.split()[1:]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=" ".join(prompt),
            temperature=0.7,
            max_tokens=400,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        msg.reply(response.choices[0].text)
import pytube
import instaloader
import facebook
@client.on_message()
def reply(msg):
    #previous code here...
    if msg.body.lower().startswith('!yt'):
        if len(msg.body.split()) > 1:
            url = msg.body.split()[1]
            yt = pytube.YouTube(url)
            yt.streams.first().download()
            client.send_message(msg.sender.id, 'Downloaded')
    elif msg.body.lower().startswith('!ig'):
        if len(msg.body.split()) > 1:
            url = msg.body.split()[1]
            loader = instaloader.Instaloader()
            loader.download_video(url)
            client.send_message(msg.sender.id, 'Downloaded')
    elif msg.body.lower().startswith('!fb'):
        if len(msg.body.split()) > 1:
            url = msg.body.split()[1]
            graph = facebook.GraphAPI(version='3.1')
            graph.get_object(id='me')
            video = graph.get_connections(id='me', connection_name='videos')
            loader = instaloader.Instaloader()
            for v in video['data']:
                loader.download_video(v['source'])
            client.send_message(msg.sender.id, 'Downloaded')
from googletrans import Translator
from microsofttranslator import Translator as MS_Translator
@client.on_message()
def reply(msg):
    #previous code here...
    translator = Translator()
    ms_translator = MS_Translator('YOUR_MICROSOFT_TRANSLATOR_API_KEY')
    if msg.body.lower().startswith('!translate'):
            lang = msg.body.split()[1]
            text = msg.body.split()[2:]
            result = translator.translate(' '.join(text), dest=lang)
            ms_result = ms_translator.translate(' '.join(text), lang)
            client.send_message(msg.sender.id, result.text+ " (Google)")
')'+ms_result+' (Microsoft)'
import sqlite3
@client.on_message()
def reply(msg):
    #previous code here...
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id text, name text, number text)''')
    c.execute('''CREATE TABLE IF NOT EXISTS feedback
                 (id text, feedback text)''')
    c.execute('''CREATE TABLE IF NOT EXISTS preferences
                 (id text, preferences text)''')
    conn.commit()
    if msg.body.lower().startswith('!saveuser'):
        if len(msg.body.split()) > 2:
            id = msg.sender.id
            name = msg.body.split()[1]
            number = msg.sender.number
            c.execute("INSERT INTO users VALUES (?, ?, ?)", (id, name, number))
            conn.commit()
    elif msg.body.lower().startswith('!savefeedback'):
        if len(msg.body.split()) > 2:
            id = msg.sender.id
            feedback = msg.body.split()[1:]
            c.execute("INSERT INTO feedback VALUES (?, ?)", (id, ' '.join(feedback)))
            conn.commit()
    elif msg.body.lower().startswith('!savepref'):
        if len(msg.body.split()) > 2:
            id = msg.sender.id
            preferences = msg.body.split()[1:]
            c.execute("INSERT INTO preferences VALUES (?, ?)", (id, ' '.join(preferences)))
            conn.commit()
admins = ['254115953912'] 
@client.on_message()
def reply(msg):
    #previous code here...
    elif msg.body.lower().startswith('!ban'):
        if msg.sender.id in admins:
            if len(msg.body.split()) > 1:
                user_id = msg.body.split()[1]
                client.block_contact(user_id)
                msg.reply('User banned')
        else:
            msg.reply('Only admins can use this command')
    elif msg.body.lower().startswith('!unban'):
        if msg.sender.id in admins:
            if len(msg.body.split()) > 1:
                user_id = msg.body.split()[1]
                client.unblock_contact(user_id)
                msg.reply('User unbanned')
        else:
            msg.reply('Only admins can use this command')
    elif msg.body.lower().startswith('!del'):
        if msg.sender.id in admins:
            if len(msg.body.split()) > 1:
                msg_id = msg.body.split()[1]
                client.delete_message(msg_id)
                msg.reply('Message deleted')
        else:
            msg.reply('Only admins can use this command')
bad_words = ['badword1', 'badword2'] 
@client.on_message()
def reply(msg):
    #previous code here...
    elif any(word in msg.body.lower() for word in bad_words):
        client.delete_message(msg.id)
    elif msg.body.lower().startswith('http'):
        client.delete_message(msg.id)
    elif len(msg.body) > 1000: 
        client.delete_message(msg.id)
jokes = ['joke1', 'joke2'] 
memes = ['meme1', 'meme2'] 
quotes = ['quote1', 'quote2']
@client.on_message()
def reply(msg):
    #previous code here...
    elif msg.body.lower().startswith('!joke'):
        joke = random.choice(jokes)
        msg.reply(joke)
    elif msg.body.lower().startswith('!meme'):
        meme = random.choice(memes)
        client.send_image(msg.sender.id, meme)
    elif msg.body.lower().startswith('!quote'):
        quote = random.choice(quotes)
        msg.reply(quote)
@client.on_message()
def reply(msg):
    #previous code here...
    elif msg.body.lower().startswith('!online'):
        client.update_status(Status.ONLINE)
        msg.reply('Status set to online')
    elif msg.body.lower().startswith('!offline'):
        client.update_status(Status.OFFLINE)
        msg.reply('Status set to offline')
    elif msg.body.lower().startswith('!status'):
        if len(msg.body.split()) > 1:
            status = msg.body.split()[1:]
            client.update_status(Status.AVAILABLE, status=' '.join(status))
            msg.reply('Status updated')
from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
class ButtonLayer(YowInterfaceLayer):
    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        if messageProtocolEntity.getType() == 'text':
            message = messageProtocolEntity.getBody()
            if message == '!button':
                buttons = [
                    {"type": "reply", "id": "1", "title": "Button 1"},
                    {"type": "reply", "id": "2", "title": "Button 2"}
                ]
                self._sendMessage(messageProtocolEntity.getFrom(), buttons)
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="database"
)
import requests
def mpesa_payment(amount, phone_number):
    api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    headers = {'Authorization': 'Bearer ACCESS_TOKEN'}
    data = {
        'BusinessShortCode': 'SHORT_CODE',
        'Password': 'PASSWORD',
        'Timestamp': 'TIMESTAMP',
        'TransactionType': 'CustomerPayBillOnline',
        'Amount': amount,
        'PartyA': phone_number,
        'PartyB': 'SHORT_CODE',
        'PhoneNumber': phone_number,
        'CallBackURL': 'CALLBACK_URL',
        'AccountReference': 'ACCOUNT_REFERENCE',
        'TransactionDesc': 'TRANSACTION_DESCRIPTION'
    }
    response = requests.post(api_url, headers=headers, json=data)
    return response.text
@client.on_event(Events.STATUS)
def status_viewed(status):
    client.status_react(status.id, StatusReact.HEART)