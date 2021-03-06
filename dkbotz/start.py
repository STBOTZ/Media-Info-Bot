# © @STBOTZ Or https://github.com/STBOTZ


import os
import urllib
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from configs import Config
#from dkbotz.command import command Not Required

@Client.on_message(filters.command("start") & filters.private)
async def start(bot: Client, cmd: Message):
    await cmd.reply_text(
        f"""**Hello {cmd.from_user.mention}**

**I Am Most Powerful Media Info Bot.**

**Use Me To Generate Infomation Of Media Like Photo, Videos And Document.**

**I Also Work in Group**""",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('➕ Add Me To Your Group ➕', url=f'http://t.me/{Config.BOT_USERNAME}?startgroup=true')
            ],[
            InlineKeyboardButton('📢 Bot Channel', url='http://t.me/STBOTZ'),
            InlineKeyboardButton('💼 Support Group', url=f'http://t.me/{Config.SUPPORT_GROUP}')
            ],[
            InlineKeyboardButton('🌐 Source Code 🌐', url='https://github.com/STBOTZ/Media-Info-Bot')
            ],[
            InlineKeyboardButton('⌦ Close The Menu ⌫', callback_data='close_data')
        ]]
        ),
     disable_web_page_preview=True
    )
