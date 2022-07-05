from userbot import bot
from telethon import events
import asyncio
from datetime import datetime
from telethon.tl.types import User, Chat, Channel

from telethon.tl.custom import Dialog
import time

def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)

@bot.on(events.NewMessage(pattern=r"\.stats", outgoing=True))
async def stats2(event):
    await event.edit("__Caricamento__")
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            broadcast_channels += 1
            if entity.creator or entity.admin_rights:
                admin_in_broadcast_channels += 1
            if entity.creator:
                creator_in_channels += 1
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        elif not isinstance(entity, Channel) and isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time
    full_name = inline_mention(await event.client.get_me())
    response = f"📊Statistiche di {full_name}\n\n"
    response += f"•👤Chat private » {private_chats} \n"
    response += f"➥👤Utenti » {private_chats - bots} \n"
    response += f"➥🤖Bot » {bots} \n"
    response += f"•👥Gruppi totali » {groups} \n"
    response += f"➥👑Proprietario » {creator_in_groups}\n"
    response += f"➥👮🏻‍♂Amministratore » {admin_in_groups}\n"
    response += f"•📣Canali » {broadcast_channels} \n"
    response += f"➥👑Proprietario » {creator_in_channels} \n"
    response += f"➥👮🏻‍♂Amministratore » {admin_in_broadcast_channels} \n"
    response += f"•🙅Mess non letti » {unread} \n"
    response += f"•#️⃣Tag non lette » {unread_mentions} \n\n"
    #response += f"tempo {stop_time:.02f}s \n"
    await event.edit(response)
