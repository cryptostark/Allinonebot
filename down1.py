import urllib
import urllib.parse
import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
import subprocess
import datetime
import asyncio
import os
import requests
import time
from p_bar import progress_bar
import aiohttp
import tgcrypto
import aiofiles
import concurrent.futures
import subprocess
from pyrogram.types import Message
from pyrogram import Client, filters
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import asyncio 
import pyrogram
from pyrogram import Client, filters, idle
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
from logging.handlers import RotatingFileHandler
LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "log.txt", maxBytes=5000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

def exec(cmd):
        process = subprocess.run(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        output = process.stdout.decode()
        error = process.stderr.decode()
        if error:
          #print(f'[error]\n{error}')
          return f'[error]\n{error}'
        if stdout:
          print(f'[stdout]\n{output}')
        #err = process.stdout.decode()
def pull_run(work, cmds):
    with concurrent.futures.ThreadPoolExecutor(max_workers=work) as executor:
        fut = executor.map(exec,cmds)
        for result in results:
	        print(result) 
bot = Client(
  "CW",
  bot_token="5717007875:AAFuDj6aaKcIT31AZmUQRg2414CcZrjdP-g",
  api_id=1654363,
  api_hash="26b911420edb5ceb8f370f21f5eb2684"
)
async def send_vid(bot,m,filename,cc,reply):
      dur = int(helper.duration(filename))
      start_time = time.time()
      try:
        await m.reply_video(filename,caption=cc, supports_streaming=True,height=720,width=1280,duration=dur)
        await reply.delete (True)
        os.remove(filename)
      except Exception: pass
  
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
                  tasks = []
                  for i in range(len(cmd)):
                    try:
                        name = (cmd[i][6])
                        cc = f'{str(count).zfill(2)}. {name} - {raw_text4}p\n\n**Batch »** {mm}\n**Dowloaded By »** {raw_text0}'
                        tasks.append(asyncio.ensure_future(send_vid(bot,m,name,cc,reply)))
                        count+=1
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
                        #reply = await m.reply_text("Uploading Video")
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
                  await asyncio.gather(*tasks)
                except Exception as e:
                  await m.reply_text(e)
    except Exception as e:
      await m.reply_text(e)
    stop_time = time.time()
    final_time = stop_time - start_time
    await m.reply_text(f"Finished in: {final_time} ")
          #continue
async def main():
        await bot.start()
        bot_info  = await bot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started (c) STARKBOT --->")
        await idle()
asyncio.get_event_loop().run_until_complete(main())
LOGGER.info(f"<---Bot Stopped-->")
            #continue