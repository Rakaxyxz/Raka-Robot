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
  LUNA += "ð´ **I'm Working Properly** \n\n"
  LUNA += "ð´ **My Master : [RakaGanteng](https://t.me/ImThelastKingMs)** \n\n"
  LUNA += f"ð´ **Telethon Version : {tlhver}** \n\n"
  LUNA += f"ð´ **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**Terimakasih Ngentot Telah menambahkan Saya â¤ï¸**"
  BUTTON = [[Button.url("Êá´Êá´", "https://t.me/raxsrobot?start=help"), Button.url("sá´á´á´á´Êá´", "https://t.me/lunasupportgroup")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  text = "â **Terimakasih Ngentot Telah Merestart**\n\nâ¢ Admin list has been **updated**"
  await tbot.send_message(event.chat_id, text)
