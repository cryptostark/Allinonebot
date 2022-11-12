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
def decode(tn):
  key = "%!$!%_$&!%F)&^!^".encode("utf8")
  iv = "#*y*#2yJ*#$wJv*v".encode("utf8")
  ciphertext = bytearray.fromhex(b64decode(tn.encode()).hex())
  cipher = AES.new(key, AES.MODE_CBC, iv)
  plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
  url=plaintext.decode('utf-8')
  return url
def encode(tn):
  key = "%!$!%_$&!%F)&^!^".encode("utf8")
  iv = "#*y*#2yJ*#$wJv*v".encode("utf8")
  ciphertext = bytearray.fromhex(b64decode(tn.encode()).hex())
  cipher = AES.new(key, AES.MODE_CBC, iv)
  url = unpad(cipher.encrypt(ciphertext), AES.block_size)
  return url
@bot.on_message(filters.command(["utkarsh"]) & ~filters.edited
async def account_login(bot: Client, m: Message):
    s = requests.Session()
    global cancel
    cancel = False
    editable = await m.reply_text(
        "Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**")
        
    cookies = {
    'csrf_name': '8b82243909b5d517bd4845e1648136b9',
    'ci_session': 'qifr600o6ovr7ll24jv03hil0jt5sdk7',}
    hdr1 = {
        'Host': 'e-utkarsh.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://e-utkarsh.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://e-utkarsh.com/',
        'Accept-Language': 'en-US,en;q=0.9'}
    info = {
        'csrf_name': '8b82243909b5d517bd4845e1648136b9',
        'mobile': '',
        'url': '0',
        'password': '',
        'submit': 'LogIn',
        'device_token': 'null',
    }
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text
    info["mobile"] = raw_text.split("*")[0]
    info["password"] = raw_text.split("*")[1]
    res1 = requests.post('https://e-utkarsh.com/web/Auth/login', cookies=cookies, headers=hdr1, data=info).json()["response"]
    re = decode(res1)
    info = {
    'type': 'Paid',
    'csrf_name': '8b82243909b5d517bd4845e1648136b9',
    'sort': '0',}
    res2 = requests.post('https://e-utkarsh.com/web/Profile/my_course', cookies=cookies, headers=hdr1, data=info).json()["response"]
    re = json.loads(decode(res2))
    open("utk.json", "a").write(json.dumps(re, indent=2))    #print(json.dumps(re, indent = 2))
    b_data = re["data"]["data"]
    cool = ""
    for data in b_data:
      t_id =data['id']
      t_name =data['title']
      FFF = "**BATCH-ID - BATCH NAME - INSTRUCTOR**"
      aa = f" ```{t_id}```  - **{t_name}**\n\n"
      if len(f'{cool}{aa}') > 4096:
          print(aa)
          cool = ""
      cool += aa
    await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
    #{"course_id":"9073","revert_api":"1#0#0#1","parent_id":0,"tile_id":"15297","layer":1,"type":"course_combo"}
    #"course_id":"4560","parent_id":"9073","layer":3,"page":1,"revert_api":"1#1#0#1","subject_id":0,"tile_id":0,"topic_id":"68324","type":"content"}
    info = {
     'tile_input':  'so6WZDcAquIgEAXgcPEvkJ8HnuugjzCKmXn0uBAW8YnU1dS7oLJFcORkuDacGqCeuOgDEt26JvCeEiQULkVfclhbBybqiCeyasz+eJyoT4kiyO65Ktep6LVrevIDD+aqR8PXMwVha16HWuZtnAD1hg==:MDE2MTA4NjQxMDI3NDUxNQ==',
    'csrf_name': '8b82243909b5d517bd4845e1648136b9'}
    res3 = requests.post('https://e-utkarsh.com/web/Course/tiles_data', cookies=cookies, headers=hdr1, data=info).json()["response"]
    re3 = json.loads(decode(res3))
    open("utk.json", "a").write(json.dumps(re3, indent=2))
    print(json.dumps(re3, indent = 2))
    b_data = re3['data']
    cool = ""
    for data in b_data:
      t_id =data['id']
      t_name =data['title']
      s_inform = data['segment_information']
      FFF = "**ID - SUBJECT NAME - INFORMATION**"
      aa = f" ```{t_id}```  - **{t_name}**  - **{s_inform}**\n\n"
      if len(f'{cool}{aa}') > 4096:
        print(aa)
        cool = ""
    cool += aa
    await m.reply_text(f'{"**You have these SUBJECTS :-**"}\n\n{FFF}\n\n{cool}')
    info = {
     'layer_two_input_data':  'eyJjb3Vyc2VfaWQiOiI0NTYwIiwicGFyZW50X2lkIjoiOTA3MyIsImxheWVyIjozLCJwYWdlIjoxLCJyZXZlcnRfYXBpIjoiMSMxIzAjMSIsInN1YmplY3RfaWQiOjAsInRpbGVfaWQiOjAsInRvcGljX2lkIjoiNjgzMjQiLCJ0eXBlIjoiY29udGVudCJ9',
     'content': 'content'
    'csrf_name': '8b82243909b5d517bd4845e1648136b9'}
    res4 = requests.post('https://e-utkarsh.com/web/Course/get_layer_two_data', cookies=cookies, headers=hdr1, data=info).json()["response"]
    re3 = json.loads(decode(res4))
    open("utk.json", "a").write(json.dumps(re3, indent=2))
    print(json.dumps(re3, indent = 2))
    b_data = re3['data']['list']
    for data in b_data:
      if data['title'] =="320p"
        url =data['url']
    
    
    
    """
    rwa_url = "https://rgvikramjeetapi.classx.co.in/post/userLogin"
    hdr = {"Auth-Key": "appxapi",
           "User-Id": "-2",
           "Authorization": "",
           "User_app_category": "",
           "Language": "en",
           "Content-Type": "application/x-www-form-urlencoded",
           "Content-Length": "233",
           "Accept-Encoding": "gzip, deflate",
           "User-Agent": "okhttp/4.9.1"
          }
    info = {"email": "", "password": ""}
    #7355971781*73559717
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text
    info["email"] = raw_text.split("*")[0]
    info["password"] = raw_text.split("*")[1]
    await input1.delete(True)
    scraper = cloudscraper.create_scraper()
    res = scraper.post(rwa_url, data=info, headers=hdr).content
    output = json.loads(res)
    #print(output)
    userid = output["data"]["userid"]
    token = output["data"]["token"]
    hdr1 = {
        "Host": "rgvikramjeetapi.classx.co.in",
        "Client-Service": "Appx",
        "Auth-Key": "appxapi",
        "User-Id": userid,
        "Authorization": token
        }
    await editable.edit("**login Successful**")
    cour_url = "https://rgvikramjeetapi.classx.co.in/get/mycourse?userid="
    res1 = s.get("https://rgvikramjeetapi.classx.co.in/get/mycourse?userid="+userid, headers=hdr1)
    b_data = res1.json()['data']
    cool = ""
    for data in b_data:
        t_name =data['course_name']
        FFF = "**BATCH-ID - BATCH NAME - INSTRUCTOR**"
        aa = f" ```{data['id']}```  - **{data['course_name']}**\n\n"
        if len(f'{cool}{aa}') > 4096:
            print(aa)
            cool = ""
        cool += aa
    await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
    editable1 = await m.reply_text("**Now send the Batch ID to Download**")
    input2 = message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    await editable1.delete(True)
    html = scraper.get("https://rgvikramjeetapi.classx.co.in/get/course_by_id?id=" + raw_text2,headers=hdr1).json()
    course_title = html["data"][0]["course_name"]
    scraper = cloudscraper.create_scraper()
    html = scraper.get("https://rgvikramjeetapi.classx.co.in/get/allsubjectfrmlivecourseclass?courseid=" + raw_text2,headers=hdr1).content
    output0 = json.loads(html)
    subjID = output0["data"]
    cool = ""
    vj = ""
    for sub in subjID:
      subjid = sub["subjectid"]
      idid = f"{subjid}&"
      subjname = sub["subject_name"]
      aa = f" ```{subjid}```  -  **{subjname}**\n\n"
      cool += aa
      vj += idid
    await editable.edit(cool)
    editable1= await m.reply_text(f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n```{vj}```")
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    await editable1.delete(True)
    prog = await editable.edit("**Extracting Videos Links Please Wait  📥 **")
    try:
        mm = "Rgvikramjeet"
        xv = raw_text3.split('&')
        for y in range(0,len(xv)):
            raw_text3 =xv[y]
            res3 = requests.get("https://rgvikramjeetapi.classx.co.in/get/alltopicfrmlivecourseclass?courseid=" + raw_text2,"&subjectid=" + raw_text3, headers=hdr1)
            b_data2 = res3.json()['data']
            for data in b_data2:
              t_name = (data["topic_name"])
              tid = (data["topicid"])
              hdr11 = {
                      "Host": "rgvikramjeetapi.classx.co.in",
                      "Client-Service": "Appx",
                      "Auth-Key": "appxapi",
                      "User-Id": userid,
                      "Authorization": token
                      }
              par = {
                  'courseid': raw_text2,'subjectid': raw_text3,'topicid': tid,'start': '-1'}
              res6 = requests.get('https://rgvikramjeetapi.classx.co.in/get/allconceptfrmlivecourseclass', params=par, headers=hdr11).json()
              b_data3 = res6['data']
              for data in b_data3:
                cid = (data["conceptid"])
                par2 = {
                'courseid': raw_text2,'subjectid': raw_text3,'topicid': tid,'conceptid': cid,'start': '-1'
                 }
                res4 = requests.get('https://rgvikramjeetapi.classx.co.in/get/livecourseclassbycoursesubtopconceptapiv3', params=par2, headers=hdr11).json()
                
                try:
                  topicid = res4["data"]
                  for data in topicid:
                      tn = (data["download_link"])
                      tid = (data["Title"])
                      url = decode(tn)
                      mtext = f"{tid}:{url}\n"
                      open(f"{mm} - {course_title}.txt", "a").write(mtext)
                except Exception as e:
                  error = f"{tid} : {e}"
                  await m.reply_text(error)
                  continue
        await prog.delete(True)        
        await m.reply_document(f"{mm} - {course_title}.txt",caption = f"```{mm} - {course_title}```" )
        os.remove(f"{mm} - {course_title}.txt")
    except Exception as e:
        await m.reply_text(str(e))
    """