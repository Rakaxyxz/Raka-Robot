import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from LunaRobot.events import register as MEMEK
from LunaRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/065bcb9beb2f286f22c61.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "**Holla I'm RaxsRobot!** \n\n"
  LUNA += "🔴 **I'm Working Properly** \n\n"
  LUNA += "🔴 **My Master : [RakaGanteng](https://t.me/ImThelastKingMs)** \n\n"
  LUNA += f"🔴 **Telethon Version : {tlhver}** \n\n"
  LUNA += f"🔴 **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**Terimakasih Ngentot Telah menambahkan Saya ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/raxsrobot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/lunasupportgroup")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  text = "✅ **Terimakasih Ngentot Telah Merestart**\n\n• Admin list has been **updated**"
  await tbot.send_message(event.chat_id, text)
