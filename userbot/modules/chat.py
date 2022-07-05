# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
"""Userbot module containing userid, chatid and log commands"""

from asyncio import sleep
from userbot.events import register

@register(outgoing=True, pattern=r"\.kickme$")
async def kickme(leave):
    """Basically it's .kickme command"""
    await leave.edit("Io vado via👋")
    await leave.client.kick_participant(leave.chat_id, 'me')
