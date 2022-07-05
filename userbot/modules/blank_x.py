SCHATSTALK_LOG='/tmp/schatstalk'
RESTART_CMD='sudo systemctl restart botrun_userbot'

from os import listdir
from os.path import isfile, join
import asyncio, os, time, random
from userbot import bot, LOGGER, LOGGER_GROUP
from telethon import events
from telethon.tl.functions.messages import SendMessageRequest, ForwardMessagesRequest
from telethon.tl.functions.channels import DeleteMessagesRequest

cstalk = None
delall = False
dt = False
announcelive = '/tmp'
bcool = False


