import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64encode, b64decode
from bs4 import BeautifulSoup
import json
import re
def decode(tn):
  key = "%!$!%_$&!%F)&^!^".encode("utf8")
  iv = "#*y*#2yJ*#$wJv*v".encode("utf8")
  ciphertext = bytearray.fromhex(b64decode(tn.encode()).hex())
  cipher = AES.new(key, AES.MODE_CBC, iv)
  plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
  url=plaintext.decode('utf-8')
  return url
csrf = "f8a2568a2d855021a7652b440aecfb8d"
session = "kv2u7tcci3n9fo3tu5pn1bqqi2dlefci"
cookies = {
    'csrf_name': csrf,
    'ci_session': session}
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
    'type': 'Paid',
    'csrf_name': csrf,
    'sort': '0',}
res2 = requests.post('https://e-utkarsh.com/web/Profile/my_course', cookies=cookies, headers=hdr1, data=info).json()["response"]
#print(res2)
ret = json.loads(decode(res2))
#open("htm.html", "a").write(re["html"])
#open("htm.json", "a").write(str(re))
html = (ret["html"])
soup = BeautifulSoup(html, 'html.parser')
subjects = soup.find('div',class_='container').find_all('div',class_='col-sm-12')
tile_ds = []
tile = []
for sub in subjects:
    links =(sub.a['href'])
    response = requests.get(links, headers=hdr1, cookies=cookies).text
    link = (re.findall("ajax_get_tiles_data\(`(.*)`",response))
    tile_ds.extend(link)
for tile_d in tile_ds:
  try:
    info = {
            'tile_input': tile_d,
            'csrf_name': csrf}
    res3 = requests.post('https://e-utkarsh.com/web/Course/tiles_data', cookies=cookies, headers=hdr1, data=info).json()["response"]
    re = json.loads(decode(res3))
    try:
      b_data = (re['data'])
      for data in b_data:
        t_id,t_title = data["id"],data["title"]
        print(t_id,t_title)
        try:
          info = {
          'course_id':  t_id,
          'parent_id': '9073',
          'csrf_name': csrf}
          res4 = requests.post('https://e-utkarsh.com/web/Course/get_course_data', cookies=cookies, headers=hdr1, data=info).json()['response']
          re = json.loads(decode(res4))
          tile_ds = (re['redirect'])
          res5 = requests.get(f"https://e-utkarsh.com/web/Course/single_book_details?id={tile_ds}", headers=hdr1, cookies=cookies).text
          link = (re.findall("ajax_get_tiles_data\(`(.*)`",res5))
          print(link)
          tile.extend(link)
          info = {
          'tile_input': tile_d,
          'csrf_name': csrf}
          res6 = requests.post('https://e-utkarsh.com/web/Course/tiles_data', cookies=cookies, headers=hdr1, data=info).json()["response"]
          tdata = json.loads(decode(res5))
          
        except:
          pass
        #re = json.loads(decode(res4))
        #print(res)
    except exception as e:
      print(e)
      pass
      continue
        
  except:pass  
"""
    
info = {
     'course_id':  '9073',
     'parent_id': '20',
    'csrf_name': '1ed59dec0b481072dfdc6e7ac2e9b0d0'}
res2 = requests.post('https://e-utkarsh.com/web/Course/get_course_data', cookies=cookies, headers=hdr1, data=info).json()['response']
re = json.loads(decode(res2))
tile_d = (re['redirect'])
red = (requests.utils.unquote(tile_d))
#re = json.loads(decode(red))
print(red)
#re = decode(d)
"so6WZDcAquIgEAXgcPEvkGh+x4XF6EZr20XPSppadnq24WJvHO7FldgHelbEvxwv:MDE2MTA4NjQxMDI3NDUxNQ=="
"so6WZDcAquIgEAXgcPEvkGh+x4XF6EZr20XPSppadnotxnRfaB/S2iao1d/JfDFj:MDE2MTA4NjQxMDI3NDUxNQ=="
"so6WZDcAquIgEAXgcPEvkJ8HnuugjzCKmXn0uBAW8YnU1dS7oLJFcORkuDacGqCeuOgDEt26JvCeEiQULkVfclhbBybqiCeyasz+eJyoT4kiyO65Ktep6LVrevIDD+aqR8PXMwVha16HWuZtnAD1hg==:MDE2MTA4NjQxMDI3NDUxNQ=="

response = requests.get('https://e-utkarsh.com/web/Course/single_book_details?id=so6WZDcAquIgEAXgcPEvkGh%2Bx4XF6EZr20XPSppadnotxnRfaB%2FS2iao1d%2FJfDFj%3AMDE2MTA4NjQxMDI3NDUxNQ%3D%3D', headers=hdr1, cookies=cookies).text
"so6WZDcAquIgEAXgcPEvkGh%2Bx4XF6EZr20XPSppadnotxnRfaB%2FS2iao1d%2FJfDFj%3AMDE2MTA4NjQxMDI3NDUxNQ%3D%3D"
soup = BeautifulSoup(response, 'html.parser')
subjects = soup.find('i',class_='fa fa-share-alt share_course')
#print(subjects["data-url"])

info = {
     'tile_input': tile_d,
    'csrf_name': '8b82243909b5d517bd4845e1648136b9'}
res3 = requests.post('https://e-utkarsh.com/web/Course/tiles_data', cookies=cookies, headers=hdr1, data=info).json()["response"]
#print(res3)
#re = json.loads(decode(res3))
#print(re)
"""
