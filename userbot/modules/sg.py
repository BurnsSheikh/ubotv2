import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register


@register(pattern="^\.sg ?(.*)", outgoing=True)
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("Rispondi al messaggio di un utente.")
       return
    reply_message = await event.get_reply_message() 
    chat = "Sangmatainfo_bot"
    sender = reply_message.sender.id
    if reply_message.sender.bot:
       await event.edit("Rispondi al messaggio di un utente.")
       return
    await event.edit("Ricerca...")
    async with event.client.conversation(chat) as conv:
          try:     
              #await conv.send_message("/search_id {}".format(sender))
              response1 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await conv.send_message("/search_id {}".format(sender))
              response1 = await response1 
              response2 = await response2 
              response3= await response3 
          except YouBlockedUserError: 
              await event.reply("SBLOCCA ( @Sangmatainfo_bot ) ")
              return
          if response1.text.startswith("No records found"):
             await event.edit("L'utente non ha mai cambiato il suo username...")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response2.message)
             
             await event.client.send_message(event.chat_id, response3.message)