#-*- coding:utf-8 -*-
import requests as req

from bs4 import BeautifulSoup as bs
import re
import time


######登录并获得session
login_url = 'https://passport.skykiwi.com/v1/login/bbslogon.do'

my_headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'Connection':'keep-alive',
    'Host':'passport.skykiwi.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

log_info = {
    'username':'nzweb',
    'password':'Utler321',
    'verifycode':'1111',
    'backurl':'http://bbs.skykiwi.com/forum.php',
    'isRemember':'0'
    }
sss = req.Session()

r = sss.get(login_url,headers = my_headers)

r = sss.post(login_url, data = log_info)

#print r.content
###########进入帖子界面，获得formhash
message_url = 'http://bbs.skykiwi.com/forum.php?mod=viewthread&tid=3616742'
message_post_url = 'http://bbs.skykiwi.com/forum.php?mod=post&action=reply&fid=205&tid=3616742&extra=&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1'
r = sss.get(message_url)
#print r.content
soup = bs(r.text,'html.parser')
formhash_tag = soup.find('input',attrs={'name':'formhash'})
#print formhash_tag
formhash = formhash_tag.attrs['value']
#print formhash

message_content = {
    'message': '【特价中】手机电脑系统安装，硬件维护，系统维护，装系统，优化系统',
    'formhash': formhash,
    'usesig': '1',
    'subject':'' 
    }
for i in range(100):
    r = sss.post(message_post_url, data = message_content)
    print r.content
    time.sleep(600)
