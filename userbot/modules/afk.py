import html

from telethon.tl import functions
from telethon.tl.functions.users import GetFullUserRequest
from userbot.events import register
from asyncio import sleep

from telethon.tl.types import MessageEntityMentionName



TMP_DOWNLOAD_DIRECTORY = "./"

async def get_user(event):
    """ Get the user from argument or replied message. """
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            await event.edit("__⚠️ » Inserisci un ID o Username valido.__")
            return None
        except:
            await event.edit("__⚠️ » Inserisci un ID o Username valido.__")

    return replied_user

@register(outgoing=True, pattern="clone(?:\s|$)([\s\S]*)")
async def _(event):
    "clone"
    replied_user = await get_user(event)
    if replied_user is None:
        return
    user_id = replied_user.id
    profile_pic = await event.client.download_profile_photo(
        user_id,
        TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",
        download_big=True
    )
    first_name = html.escape(replied_user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    replied_user = await event.client(GetFullUserRequest(replied_user.id))
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = replied_user.about
    await event.client(functions.account.UpdateProfileRequest(first_name=first_name))
    await event.client(functions.account.UpdateProfileRequest(last_name=last_name))
    await event.client(functions.account.UpdateProfileRequest(about=user_bio))
    try:
        pfile = await event.client.upload_file(profile_pic)
    except Exception as e:
        return await event.edit(event, f"Errore")
    await event.client(functions.photos.UploadProfilePhotoRequest(pfile))
    await event.edit(event, "**Profilo clonato con successo**")

