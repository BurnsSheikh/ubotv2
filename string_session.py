import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pyrogram import Client

select = " "

docs = """Generate your Telegram String Session
P -->> Pyrogram [https://docs.pyrogram.org]
T -->> Telethon [https://docs.telethon.dev]
"""

tutor = """
~ go-to my.telegram.org
~ Login using your Telegram account
~ Click on API Development Tools
~ Create a new application, by entering the required details
~ Check your Telegram saved messages section to copy the STRING_SESSION
"""

template = """
{}
"""


print(docs)

while select != ("p", "t"):
    select = input("Enter your required client < p / t > : ").lower()
    if select == "t":
        print("""\nTelethon selected\nRunning script...""")
        time.sleep(1)
        print(tutor)
        API_KEY = 7480744
        API_HASH = '8cd929c96311aaaa3674a9fd0c7f7e0b'
        proxy = {
    'proxy_type': 'socks5', # (mandatory) protocol to use (see above)
    'addr': '',      # (mandatory) proxy IP address
    'port': ,           # (mandatory) proxy port number
    'username': '',      # (optional) username if the proxy requires auth
    'password': '',      # (optional) password if the proxy requires auth
    'rdns': True            # (optional) whether to use remote or local resolve, default remote
}
        
    elif select == "p":
        with TelegramClient(StringSession(), API_KEY, API_HASH, proxy=proxy) as client:
            session_string = client.session.save()
            #saved_messages_template = "Telethon session" + template.format(session_string)
            print("\nGenerating String Session...\n")
            #client.send_message("me", saved_messages_template, parse_mode="html")
            time.sleep(1)
            print(session_string)
        break

    elif select == "p":
        print("""\nUsa telethon...""")

    
    else:
        print("\nt o p\n")
        time.sleep(1.5)