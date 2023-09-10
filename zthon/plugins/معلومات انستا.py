import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from zthon import zedub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البحث"


ZelzalPH_cmd = (
    "𓆩 [S��𐍂�� ���� - مـعلـومـات الإنستجـرام](t.me/aud9i) 𓆪\n\n"
    "**⪼ الأمــر ↵**\n\n"
    "⪼ `.معلومات انستا` + @يوزر الحساب\n\n"
    "\n𓆩 [بيدو](t.me/billdu) 𓆪"
)


@zedub.zed_cmd(
    pattern="معلومات انستا ?(.*)",
    command=("معلومات انستا", plugin_category),
    info={
        "header": "يستخدم هـذا الأمـر لجلـب معلومـات حـساب الإنستجرام",
        "الاسـتـخدام": "{tr}معلومات انستا + @يوزر الحساب",
    },
)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╾ ╿يـرجـى استخـدام الأمـر بالشكـل الصحيـح ( .معلومات انستا + @معرف الحساب )**"
        )
    chat = "@infstabot"
    zzzzl1l = await edit_or_reply(event, "**جـاري جـلب معلـومـات حسـاب الإنستجـرام ⧫ ....**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1194140165)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzzzl1l.edit("**• ⎙ | تأكـد مـن أنـك لم تقـم بحظـر البـوت @infstabot**")
            return
        if response.text.startswith("I can't find that"):
            await zzzzl1l.edit("**• عـذرًا لم أستطـع معرفـة معلومـات الحسـاب تأكد من أنك أدخلتـه بالشكـى الصحيـح**")
        else:
            await zzzzl1l.delete()
            await event.client.send_message(event.chat_id, response.message)



@zedub.zed_cmd(pattern="معلومات الانستجرام")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalPH_cmd)

