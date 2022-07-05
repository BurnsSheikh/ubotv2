
import os
import asyncio
import json
from telethon.tl.functions.channels import CreateChannelRequest, CheckUsernameRequest, UpdateUsernameRequest
from telethon.tl.types import InputChannel, InputPeerChannel
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.account import UpdateUsernameRequest as UUpdateUsernameRequest
from telethon import functions, types
from userbot.events import register

@register(outgoing=True, pattern="^.forward(?: |$)(.*)")
async def forward(event):
    reply_message = await event.get_reply_message() 
    msg = await reply_message.forward_to(-1001170219096)
    await event.edit("✅ Messaggio inoltrato correttamente")