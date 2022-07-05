import asyncio
from userbot import bot
from userbot import (AFKREASON, COUNT_MSG, ISAFK, LOGGER, LOGGER_GROUP, USERS)
from userbot import (COUNT_PM, HELPER, LOGGER, LOGGER_GROUP, NOTIF_OFF,
                     PM_AUTO_BAN, BRAIN_CHECKER, LASTMSG, LOGS)
from userbot import (LOGGER)
from userbot.events import register
from telethon.tl.functions.account import UpdateProfileRequest
from telethon import events
from telethon.events import StopPropagation
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon import functions, types
import requests
from telethon.tl.functions.messages import GetAllChatsRequest
from googletrans import Translator
import os
import json

message = ""
exempt = []
mutedList = []
autoNiceText = False
autoReplyPvt = False



@register(outgoing=True, pattern="^[.]creator$")
async def cre(e):
  await e.edit("""🧑🏻‍💻 Userbot sviluppato da @ItsMat
♻️ Canale @ItsMatDev""")

@register(outgoing=True, pattern="^[.]dev$")
async def dev(e):
  await e.edit("""🧑🏻‍💻 Userbot sviluppato da @ItsMat
♻️ Canale @ItsMatDev""")

@register(outgoing=True, pattern="^[.]seller$")
async def seller(e):
  await e.edit("""🧑🏻‍💻 Userbot sviluppato da @ItsMat
♻️ Canale @ItsMatDev""")



@register(outgoing=True, pattern="^.pula$")
async def CARABINIERIIIIIIIIIII(e):
  for i in range(10):
    await asyncio.wait([e.edit("🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴")])
    await asyncio.sleep(0.1)
  await asyncio.wait([e.edit("**🚓 SCAPPA, ARRIVA LA PULA 🚓**")])

@register(outgoing=True, pattern="^.ficca$")
async def ficca(e):
  for i in range(5):
    await asyncio.wait([e.edit("👉🏻👌🏻 OHH")])
    await asyncio.sleep(0.2)
    await asyncio.wait([e.edit("👉🏻 👌🏻OHH SII ")])
    await asyncio.sleep(0.2)
    await asyncio.wait([e.edit("👉🏻  👌🏻OOOOOOH ")])
    await asyncio.sleep(0.2)
  await asyncio.wait([e.edit("OHH SIII!")])


@register(outgoing=True, pattern="^[.]cb")
async def cb(e):
  bio = e.text.split(" ", 1)[1]
  await bot(UpdateProfileRequest(about=bio))
  await e.edit("✅ Biografia modificata con successo.")

@register(outgoing=True, pattern="^[.]help")
async def comandi(e):
	await asyncio.wait([e.edit("[🔗Clicca qui](https://telegra.ph/Comandi-UserBot-20-09-14)")])

@register(outgoing=True, pattern="^[.]cmd")
async def cmd(e):
	await asyncio.wait([e.edit("[🔗Clicca qui](https://telegra.ph/Comandi-UserBot-20-09-14)")])

@register(outgoing=True, pattern="^[.]aiuto")
async def aiuto(e):
	await asyncio.wait([e.edit("[🔗Clicca qui](https://telegra.ph/Comandi-UserBot-20-09-14)")])

@register(outgoing=True, pattern="^[.]cmds")
async def cmds(e):
	await asyncio.wait([e.edit("[🔗Clicca qui](https://telegra.ph/Comandi-UserBot-20-09-14)")])
#BTC
@register(outgoing=True, pattern="^[.]btc$")
async def bitCoinezzss(e):
  await e.edit("**Prezzo: " + str(requests.get("https://blockchain.info/ticker").json()["USD"]["last"]) + " USD**")

@register(outgoing=True, pattern="^[.]btceur$")
async def bitCoinezzss(e):
  await e.edit("**Prezzo: " + str(requests.get("https://blockchain.info/ticker").json()["EUR"]["last"]) + " EUR**")

#CALC
@register(outgoing=True, pattern="^[.]calc ")
async def Calcolozzs(e):
  st = e.text.split(" ")
  if st.__len__() == 4:
    if st[2] == "+":
      r = float(st[1].replace(",", ".")) + float(st[3].replace(",", "."))
      await e.edit(f"__Operazione eseguita__:** {st[1]} + {st[3]}\nRisultato: {r}**")
    elif st[2] == "-":
      r = float(st[1].replace(",", ".")) - float(st[3].replace(",", "."))
      await e.edit(f"__Operazione eseguita__:** {st[1]} - {st[3]}\nRisultato: {r}**")
    elif st[2] == "x" or st[2] == "×" or st[2] == "*":
      r = float(st[1].replace(",", ".")) * float(st[3].replace(",", "."))
      await e.edit(f"__Operazione eseguita__:** {st[1]} × {st[3]}\nRisultato: {r}**")
    elif st[2] == ":" or st[2] == "/" or st[2] == "÷":
      r = float(st[1].replace(",", ".")) / float(st[3].replace(",", "."))
      await e.edit(f"__Operazione eseguita__:** {st[1]} : {st[3]}\nRisultato: {r}**")
  else:
    await e.edit("**Errore**")

#GROUPLIST & CHANNELLIST
@register(outgoing=True, pattern="^[.]listagruppi$")
async def groupList(e):
  chats = await e.client(GetAllChatsRequest([]))
  groups = []
  for i in chats.chats:
    if type(i).__name__ == "Channel":
      if i.megagroup and not i.left:
        groups.append(f"__{i.title}__ - [`{i.id}`]")
    elif type(i).__name__ == "Chat":
      if not i.left and not i.kicked and not i.deactivated:
        groups.append(f"__{i.title}__ - [`{i.id}`]")
  mex = "**LISTA GRUPPI**\n"
  for i in groups:
    mex += f"\n{i}"
  await e.edit(mex)

@register(outgoing=True, pattern="^[.]listacanali$")
async def channelList(e):
  chats = await e.client(GetAllChatsRequest([]))
  chann = []
  for i in chats.chats:
    if type(i).__name__ == "Channel":
      if not i.megagroup and not i.left:
        chann.append(f"__{i.title}__ - [`{i.id}`]")
  mex = "**LISTA CANALI**\n"
  for i in chann:
    mex += f"\n{i}"
  await e.edit(mex)


#PURGE
@register(outgoing=True, pattern="^[.]purge$")
async def Purge(e):
  if e.is_reply:
    chat = await e.get_input_chat()
    msgs = []
    count = 0
    async for msg in e.client.iter_messages(chat, min_id=e.reply_to_msg_id):
      msgs.append(msg)
      count += 1
      msgs.append(e.reply_to_msg_id)
      if len(msgs) == 100:
        await e.client.delete_messages(chat, msgs)
        msgs = []
    if msgs.__len__() > 0:
      await e.client.delete_messages(chat, msgs)
  else:
    await e.edit("⚠️ Nessun messaggio selezionato.")

#Verify
verify = None

@register(outgoing=True, pattern="^[.]verify$")
async def Verify(e):
  global verify
  verify = e
  await e.client.send_message("@SpamBot", "/start")

@register(incoming=True)
async def checkVerify(e):
  global verify
  if verify != None:
    if e.chat_id == 178220800:
      if ":" in e.text:
        st = e.text.split(" ")
        for i in range(st.__len__()):
          if ":" in st[i]:
            fine = st[i - 3] + " " + st[i - 2] + " " + st[i - 1] + " Ore: " +st[i]
            break
        await verify.edit(f"""⚠️ Al momento **sei limitato!**
Le limitazioni termineranno il {fine}.""")
        verify = None
        await e.client(functions.messages.DeleteHistoryRequest(e.chat_id, 0, False, True))
      else:
        await verify.edit("✅ Al momento **non** esiste alcuna limitazione sul tuo account.")
        verify = None
        await e.client(functions.messages.DeleteHistoryRequest(e.chat_id, 0, False, True))

#FILTER
if not os.path.exists("storage.json"):
  with open("storage.json", "w+") as f:
    data = {}
    data["filtri"] = []
    data["reply"] = []
    json.dump(data, f)

@register(outgoing=True, pattern="^[.]addfiltro ")
async def setFilter(e):
  with open("storage.json", "r") as f:
    data = json.load(f)
  filtro = e.text.split(" ")[1]
  st = e.text.split(" ", 2)
  if st.__len__() == 3:
    if not "filtri" in data or not st[1] in data["filtri"]:
      data["filtri"].append(st[1])
      data["reply"].append(st[2])
      with open("storage.json", "w+") as f:
        json.dump(data, f)
      await e.edit(f"✅ Filtro {filtro} aggiunto.")
    else:
      await e.edit("⚠️ Il filtro è già presente.")
  else:
    await e.edit("⚠️ Errore")

@register(outgoing=True, pattern="^[.]delfiltro ")
async def unFilter(e):
  filtro = e.text.split(" ")[1]
  with open("storage.json", "r") as f:
    data = json.load(f)
  if "filtri" in data and filtro in data["filtri"]:
    for i in range(data["filtri"].__len__()):
      if data["filtri"][i] == filtro:
        data["reply"].remove(data["reply"][i])
        break
    await e.edit(f"✅ Filtro {filtro} rimosso.")
    data["filtri"].remove(filtro)
    with open("storage.json", "w+") as f:
      json.dump(data, f)
  else:
    await e.edit(f"⚠️ Il filtro .{filtro} è inesistente.")

@register(outgoing=True, pattern="^[.]filtri$")
async def filterList(e):
  with open("storage.json", "r") as f:
    data = json.load(f)
  filtri = "**✍🏻 Lista filtri**\n"
  if "filtri" in data:
    for i in data["filtri"]:
      filtri += "\n- " + i
  await e.edit(filtri)

@register(outgoing=True)
async def Filter(e):
  with open("storage.json", "r") as f:
    data = json.load(f)
  if "filtri" in data:
    for i in range(data["filtri"].__len__()):
      if e.text.lower() == data["filtri"][i].lower():
        await e.edit(data["reply"][i])
        break

@register(outgoing=True, pattern="^[.]type ")
async def niceText(e):
  split = e.text.split(" ", 1)
  if split.__len__() >= 2:
    text = split[1]
    mex = ""
    for i in range(len(text)):
      if text[i] == " ":
        mex = mex + ' '
      else:
        mex = mex + text[i]
      await asyncio.wait([e.edit("`" + mex + " |`")])
      await asyncio.sleep(0.1)
      await asyncio.wait([e.edit("`" + mex + "  ‏‏‎ `")])
      await asyncio.sleep(0.1)
      if i == len(e.text) - 1:
        await asyncio.wait([e.edit("`" + e.text + "`")])

#BLOCK & UNBLOCK


#ON & OFF
@register(outgoing=True, pattern="^[.]on$")
async def changeNameON(e):
  global ON
  await bot(UpdateProfileRequest(last_name="[Online]"))
  await e.edit("✅ Stato impostato su Online!")

@register(outgoing=True, pattern="^[.]off$")
async def changeNameOFF(e):
  global OFF
  await bot(UpdateProfileRequest(last_name="[Offline]"))
  await e.edit("✅ Stato impostato su Offline!")
  
  

@register(outgoing=True, pattern="^.niceText$")
async def setNiceText(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    global autoNiceText
    if autoNiceText:
      autoNiceText = False
      await e.edit("🎈 » Animazione disattivata")
    else:
      autoNiceText = True
      await e.edit("🎈 » Animazione attivata")


#mute




@register(outgoing=True, pattern="^[.]block$")
async def fdsfsdfs(e):
  if not (await e.get_sender()).bot:
    global BLOCKMESSAGGIO
    if e.is_reply:
      reply = await e.get_reply_message()
      name = reply.sender.first_name
      idutente = reply.sender.id
      await e.delete()
      await e.client.send_message(reply.chat_id, f'✅ <a href="tg://user?id={idutente}">{name}</a> [<code>{idutente}</code>] bloccato correttamente.', reply_to=reply, parse_mode="html")
      await e.client(BlockRequest(reply.sender.id))
    else:
      if e.is_private:
        idutente = e.chat_id
        name = e.chat.first_name
        await e.edit(f'✅ <a href="tg://user?id={idutente}">{name}</a> [<code>{idutente}</code>] bloccato correttamente.', parse_mode="html")
        await e.client(BlockRequest(e.chat_id))


@register(outgoing=True, pattern="^.unblock$")
async def unblockUser(e):
  if not e.text[0].isalpha():
    if not (await e.get_sender()).bot:
      global UNBLOCKMESS
      if e.is_reply:
        reply = await e.get_reply_message()
        name = reply.sender.first_name
        idutente = reply.sender.id
        await e.delete()
        await e.client.send_message(reply.chat_id, f'✅ <a href="tg://user?id={idutente}">{name}</a> [<code>{idutente}</code>] bloccato correttamente.', reply_to=reply, parse_mode="html")
        await e.client(UnblockRequest(reply.sender.id))
      else:
        if e.is_private:
          idutente = e.chat_id
          name = e.chat.first_name
          await e.edit(f'✅ <a href="tg://user?id={idutente}">{name}</a> [<code>{idutente}</code>] sbloccato correttamente.', parse_mode="html")
          await e.client(UnblockRequest(e.chat_id))

@register(outgoing=True, pattern="^[.]archive$")
async def archiveChat(e):
  for d in await e.client.get_dialogs(limit=None, ignore_migrated=True):
      if d.entity.id == e.chat_id:
          if d.archived:
              await e.edit("❌ La chat era già archiviata")
          else:
              await d.archive()
              await e.edit("✅ Chat archiviata")
          break
        
    

@register(outgoing=True, pattern="^[.]unarchive$")
async def unarchiveChat(e):
    for d in await e.client.get_dialogs(limit=None, ignore_migrated=True):
        if d.entity.id == e.chat_id:
            if d.archived:
                await d.archive(folder=0)
                await e.edit("✅ Chat Unarchiviata")
            else:
                await e.edit("❌ La chat non era archiviata")
            break

@register(outgoing=True, pattern="^[.]mute$")
async def setMute(e):
	global SAVES
	if e.is_private and not (await e.get_sender()).bot:
		if e.chat_id in SAVES["mutedList"]:
			SAVES["mutedList"].remove(e.chat_id)
			'(save)'
			await e.edit(f"""🔉 {e.chat_id} smutato correttamente.
Da ora potrà scriverti unicamente in privato.""")
		else:
			SAVES["mutedList"].append(e.chat_id)
			'(save)'
			await e.edit(f"""🔇 {e.chat_id} mutato correttamente.
__Da ora non potrà più scriverti in privato.__""")
		
@register(incoming=True)
async def muteManager(e):
	global SAVES
	if e.is_private and not (await e.get_sender()).bot and e.chat_id in SAVES["mutedList"]:
		await e.delete()
		
		
if os.path.exists("saves.json"):
	with open("saves.json", "r+") as f:
		SAVES = json.load(f)
else:
	SAVES = {"AFKMode": False, "Approved": [], "mutedList": [], "AFK-Mex": "Puoi customizzare il seguente messaggio con .msgafk", "Block-Mex": "Imposta il messaggio con .msgblock"}
	with open("saves.json", "w+") as f:
		json.dump(SAVES, f)
	

async def save():
	global SAVES
	with open("saves.json", "w+") as f:
		json.dump(SAVES, f)



inWait = []
	
@register(outgoing=True, pattern="^[.]msgafk")
async def setAFKMex(e):
	global SAVES
	st = e.text.split(" ", 1)
	if st.__len__() == 2:
		SAVES["AFK-Mex"] = st[1]
		'(save)'
		await e.edit('✅ Messaggio AFK impostato.')
	else:
		await e.edit('''⚠️ Impostare un messaggio!
Il comando da eseguire è .msgafk {messaggio}.''')
  

@register(outgoing=True, pattern="^[.]afk$")
async def setAFK(e):
	global SAVES
	if SAVES["AFKMode"]:
		SAVES["AFKMode"] = False
		'(save)'
		await e.edit("✅ Modalità AFK disattivata.")
	else:
		SAVES["AFKMode"] = True
		'(save)'
		await e.edit("✅ Modalità AFK attivata.")
	
@register(outgoing=True, pattern="^[.]approve$")
async def approveUser(e):
	global SAVES
	if e.chat_id in SAVES["Approved"]:
		await e.edit("⚠️ Questa chat è già approvata.")
	else:
		SAVES["Approved"].append(e.chat_id)
		'(save)'
		await e.edit(f"✅ Chat {e.chat_id} approvata.")
	
@register(outgoing=True, pattern="^[.]disapprove$")
async def disapproveUser(e):
	global SAVES
	if e.chat_id in SAVES["Approved"]:
		SAVES["Approved"].remove(e.chat_id)
		'(save)'
		await e.edit(f"✅ Chat {e.chat_id} disapprovata.")
	else:
		await e.edit("⚠️ Questo utente non è approvato.")
	

@register(incoming=True)
async def doAFK(e): 
	global SAVES, inWait
	if SAVES["AFKMode"] and e.is_private and not (await e.get_sender()).bot and not e.chat_id in SAVES["Approved"]:
		await e.delete()
		if not e.chat_id in inWait: 
			inWait.append(e.chat_id)
			if e.text == None or e.text == "":
				mex = "__MEDIA__"
			else:
				mex = e.text
			await e.respond(SAVES["AFK-Mex"].replace("{msg}", mex))
			await asyncio.sleep(30)
			inWait.remove(e.chat_id)		
		