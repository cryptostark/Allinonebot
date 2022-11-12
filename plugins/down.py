
#  MIT License
#
#  Copyright (c) 2019-present Dan <https://github.com/delivrance>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE
#  Code edited By Cryptostark
import urllib
import urllib.parse
import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import pyrogram
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
import time
from pyrogram.types import User, Message
from p_bar import progress_bar
import subprocess
from subprocess import getstatusoutput
import logging
import os
import sys
import re
from pyrogram import Client as bot
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64encode, b64decode

@bot.on_message(filters.command(["down"]) & ~filters.edited)
async def account_login(bot: Client, m: Message):
    global cancel
    cancel = False
    editable = await m.reply_text("**Send Text file containing Urls**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/"

    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return
    editable = await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text
    try:
        arg = int(raw_text)
    except:
        arg = 0
    editable = await m.reply_text("**Enter Batch Name**")
    input01: Message = await bot.listen(editable.chat.id)
    mm = input01.text    
    await m.reply_text("**Downloaded By**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text
    
    await m.reply_text("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text4 = input2.text

    editable4= await m.reply_text("Now send the **Thumb url**\nEg : ```https://telegra.ph/file/cef3ef6ee69126c23bfe3.jpg```\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
        
    if raw_text =='0':
        count =1
    else:       
        #count =int(raw_text)
        count = int(raw_text)
    await m.reply_text("**Enter No Threads**")
    input12: Message = await bot.listen(editable.chat.id)
    raw_text12 = input12.text
    thread = int(raw_text12)
    clist = []
    for i in range(arg, len(links)):
        try:
          url = links[i][1]
          name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@","").replace("*","").replace(".","").strip()
        except IndexError:
          pass
        if "youtu" in url:
            clist.append(['yt-dlp','-S',f'height:{raw_text4},ext:mp4','-N','100','-o',f'{name1}.mp4',url])
        elif ".pdf" in url:
            clist.append(['yt-dlp','-o',f'{name1}.pdf',url])
        else:
          clist.append(['yt-dlp','-S',f'height:{raw_text4},ext:mp4','-N','100','-o',f'{name1}.mp4',url])
    try:
        for i in range(0, len(clist),thread):
                cmd = clist[i: i + thread]
                #print(cmd)
                Show = f"**Downloading Videos**\n"
                prog = await m.reply_text(Show)
                try:
                  helper.pull_run(thread,cmd)
                  for i in range(len(cmd)):
                    try:
                        name = (cmd[i][6])
                    except:
                        name= cmd[i][2]
                    #print(name)
                    await prog.delete (True)
                    if "pdf" in name:
                        #print("pdf found")
                        cc2 = f'{str(count).zfill(2)}. {name}\n\n**Batch »** {mm}\n**Dowloaded By »** {raw_text0}'
                        await m.reply_document(name,caption=cc2)
                        os.remove(f"{name}")
                        count+=1
                        continue 
                    else:
                        #print("Video found")
                        reply = await m.reply_text("Uploading Video")
                        try:
                            if thumb == "no":
                                thumbnail = f"{name}.jpg"
                            else:
                                thumbnail = "thumb.jpg"
                        except Exception as e:
                            await m.reply_text(str(e))
                            continue
                        await prog.delete (True)
                        start_time = time.time()
                        cc = f'{str(count).zfill(2)}. {name} - {raw_text4}p\n\n**Batch »** {mm}\n**Dowloaded By »** {raw_text0}'
                        dur = int(helper.duration(name))
                        subprocess.run(f'ffmpeg -i "{name}" -ss 00:01:00  -y -vframes 1 "{name}.jpg"', shell=True)
                        await m.reply_video(f"{name}",caption=cc, supports_streaming=True,height=720,width=1280,thumb=thumbnail,duration=dur,progress=progress_bar,progress_args=(reply,start_time))
                        count+=1
                        os.remove(f"{name}")
                        os.remove(f"{name}.jpg")
                        await reply.delete (True)
                except Exception as e:
                  await m.reply_text(e)
                  continue
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")
            #continue