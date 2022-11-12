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
from jinja2 import Template
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
from subprocess import getstatusoutput
import logging
import os
import sys
import re
from pyrogram import Client as bot
import cloudscraper
import base64

@bot.on_message(filters.command(["chandra"]) & ~filters.edited)
async def account_login(bot: Client, m: Message):
    template  = Template(open("template.html").read())
    s = requests.Session()
    global cancel
    mm = "Chandra"
    cancel = False
    editable = await m.reply_text(
        "Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**")
     
    login_url = "http://api.chandrainstitute.com/api/v2/api.php/user/login"
    info = {
    "mobile": "",
    "password": "",
    "android_id": "asdasdasda"
    }
    
    auth = "7b81679d-a829-4476-8dcf-9c3bb4e0c80a"
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text
    info["mobile"] = raw_text.split("*")[0]
    info["password"] = raw_text.split("*")[1]   
    res = s.post(login_url, data=json.dumps(info), headers={"Auth":auth})
    login_res = res.json()
    login_dict = login_res["response"]
    u_id, token = login_dict["u_id"], login_dict["auth_token"]
    if len(u_id)>0:
      pass
    else:
      editable = await m.reply_text("Login Failed Check Response")
    await input1.delete(True)
    
    all_course_link = "http://api.chandrainstitute.com/api/v2/api.php/get/all/course"
    new_info = {
    "user_id": u_id,
    "course_type": "videos",
    "payment_type": "paid"
    }
    courses_res = s.post(all_course_link, data=json.dumps(new_info), headers={"Auth":auth, "token": token})
    b_data = courses_res.json()["response"]
    cool = ""
    vj = ""
    for course_dict in  b_data:
      course_id, course_title = course_dict["cp_id"], course_dict["title"]
      FFF = "**BATCH-ID - BATCH NAME**"
      idid = f"{course_id}&"
      aa = f" ```{course_id}```  - **{course_title}**\n\n"
      # aa=f"**Batch Name -** {data['batchName']}\n**Batch ID -** ```{data['id']}```\n**By -** {data['instructorName']}\n\n"
      if len(f'{cool}{aa}') > 4096:
          print(aa)
          cool = ""
      cool += aa
      vj += idid
    editable = await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
    editable1= await m.reply_text(f"Now send the **Batch IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download All Batches :-**\n```{vj}```")
    input2 = message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    
    await input2.delete(True)
    await editable.delete(True)
    try:
        xv = raw_text2.split('&')
        for y in range(0,len(xv)):
            t =xv[y]
            prog = await editable1.edit("**Extracting Videos Links Please Wait  🔴 **")
            course_link = f"http://api.chandrainstitute.com/pdo/api/api.php/get/list/subjects/videos/all/{t}"
            course_res = s.get(course_link, headers={"Auth":auth, "token": token})
            try:
                subjects = course_res.json()["response"]
            except:
                continue 
            output_dict = {}
            for subject in subjects:
              subject_id, subject_name = subject["subject_id"], subject["subject_name"]
              subject_title = f"{subject_id}. {subject_name}"
              subject_link = "http://api.chandrainstitute.com/api/v2/api.php/get/class/all/chapters/list"
              subject_info = {
               "course_id": course_id,
               "subject_id": subject_id,
               "u_id": u_id
              }
              subject_res = s.post(subject_link, data=json.dumps(subject_info), headers={"Auth":auth, "token": token})
              try:
                chapters = subject_res.json()["response"]
                #open(f"{course_id}.json", "w").write(json.dumps(chapters, indent=4))
              except:
                continue
              videos_dict = {}
              for chapter in chapters:
                  chapter_id = chapter["chapter_id"]
                  chapter_name = chapter["chapter_name"].strip()
                  youtube_id = chapter["youtubeId"]
                  video_id = base64.b64decode(youtube_id).decode("UTF-8")
                  video_link = f"https://youtu.be/{video_id}"
                  video_title = f"{chapter_name}"
                  videos_dict[video_title] = video_link
                  mtext = f"{subject_name} - {chapter_name}:{video_link}\n"
                  open(f"{mm} - {course_title}.txt", "a").write(mtext)
                  output_dict[subject_title] = videos_dict
              
              notes_link = "http://godaddy.chandrainstitute.com/api/V2/devapi.php/get/class/notes/v1/list"
              subject_info = {
             "cc_id": course_id,
             "subject_id": subject_id,
             "u_id": u_id,
             "notes_type": "lecture"
              }
              subject_res = s.post(notes_link, data=json.dumps(subject_info), headers={"Auth":auth, "token": token})
              try:
                notes = subject_res.json()["response"][0]
                print(notes)
                note_title = notes["title"]
                notes_url = notes["notes_url"]
                mtext = f"{note_title}:{notes_url}\n"
                open(f"{mm} - {course_title}.txt", "a").write(mtext)
                #output_dict[subject_title] = notes_dict
              except:
                continue
            prog = await editable1.edit("**Extracting Links Please Wait🟢  **")          
        await prog.delete(True)         
        await m.reply_document(f"{mm} - {course_title}.txt",caption = f"```{mm} - {course_title}```" )
        #open(f"{mm} - {course_title}.html", "a").write(template.render(title=course_title, batch=course_title, topics=output_dict, type="videos"))
        #open(f"{mm} - {course_title}.html", "a").write(template.render(title=course_title, batch=course_title, topics=output_dict, type="notes"))
        #await m.reply_document(f"{mm} - {course_title}.html",caption = f"**{mm} - {course_title}**\n (Html Webpage) ")
    except Exception as e:
        await m.reply_text(str(e))
    os.remove(f"{mm} - {course_title}.txt")
    #os.remove(f"{mm} - {course_title}.html")
          