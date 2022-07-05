from telethon import TelegramClient, events
API_KEY="Type that here"
API_HASH="Type that here"
proxy = {
    'proxy_type': 'socks5', # (mandatory) protocol to use (see above)
    'addr': '1.1.1.1',      # (mandatory) proxy IP address
    'port': 5555,           # (mandatory) proxy port number
    'username': 'foo',      # (optional) username if the proxy requires auth
    'password': 'bar',      # (optional) password if the proxy requires auth
    'rdns': True            # (optional) whether to use remote or local resolve, default remote
}
#get it from my.telegram.org
bot = TelegramClient('userbot',API_KEY,API_HASH, proxy)
bot.start()

#This script wont run your bot, it just generates a session.
