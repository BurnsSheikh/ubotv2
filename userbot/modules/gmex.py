from telethon import functions, types
from userbot.events import register
import os, json, asyncio

if os.path.exists("gruppigmex.json"):
    with open("gruppigmex.json", "r+") as f:
        Groups = json.load(f)
else:
    Groups = {}
    with open("gruppigmex.json", "w+") as f:
      json.dump(Groups, f)

async def updateGroups():
    global Groups
    with open("gruppigmex.json", "w+") as f:
        json.dump(Groups, f)
    return True

@register(outgoing=True, pattern="^[.]gmex")
async def GmexFunction(e):
    global Groups
    st = e.text.split(" ", 1)
    if len(st) == 2:
        if len(Groups) > 0:
            await e.edit("__🔄 Gmex in corso...__")
            await asyncio.wait([e.client.send_message(int(chat), st[1]) for chat in Groups])
            await e.edit(f"""✅ Gmex completato con successo.""")
        else:
            await e.edit("⚠️ Non hai impostato nessun gruppo in cui gmexare il messaggio.")
    else:
         await e.edit("⚠️ Messaggio non impostato.")

@register(outgoing=True, pattern="^[.]addgroup")
async def addChat(e):
    global Groups
    st = e.text.replace("-100", "").split(" ", 1)
    if len(st) == 2:
        if st[1].isnumeric():
            mex = int(st[1])
        else:
            mex = st[1]
        try:
            group = await e.client.get_entity(mex)
        except:
            await e.edit(f"⚠️ Chat non trovata!")
            return
        if type(group).__name__ == "User":
            await e.edit("⚠️ Puoi aggiungere solo gruppi e canali.")
            return
        if not str(group.id) in Groups:
            Groups[str(group.id)] = group.title
            await updateGroups()
            await e.edit(f"✅ Chat {group.title} aggiunta alla lista gruppi del gmex.")
        else:
            await e.edit(f"⚠️ Errore » {group.title} già presente in lista")
    else:
        await e.edit("⚠️ Chat non trovata!")

@register(outgoing=True, pattern="^[.]delgroup")
async def remChat(e):
    global Groups
    st = e.text.replace("-100", "").split(" ", 1)
    if len(st) == 2:
        if st[1].isnumeric():
            mex = int(st[1])
        else:
            mex = st[1]
        try:
            group = await e.client.get_entity(mex)
        except:
            await e.edit("⚠️ Chat non trovata!")
            return
        if str(group.id) in Groups:
            del Groups[str(group.id)]
            await updateGroups()
            await e.edit(f"✅ Chat {group.title} rimossa dalle lista gruppi del gmex.")
        else:
            await e.edit(f"⚠️ Errore » {group.title} non presente in lista**")
    else:
        await e.edit("⚠️ Chat non trovata!")

@register(outgoing=True, pattern="^[.]gruppi$")
async def chatsList(e):
    global Groups
    if len(Groups) > 0:
        msg = "**👥 Lista gruppi gmex**\n"
        for id in Groups:
            msg += "\n» " + Groups[id] + f" [`-100{id}`]"
        await e.edit(msg + "\n\n✔️ Totale chat aggiunte » " + str(len(Groups)) + "")
    else:
        await e.edit('''**👥 Lista gruppi gmex**

⚠️ Nessuna chat è stata aggiunta alla lista gruppi del gmex! 

✔️ Totale chat aggiunte » 0''')