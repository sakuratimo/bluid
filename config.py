import requests
import re
import sys

def setlag(host):
    burp0_url = "http://"+host+"/install.php?language=zh_CN"
    burp0_headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/install.php", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    requests.get(burp0_url, headers=burp0_headers)

def setadmin(host):
    burp0_url = "http://"+host+"/install.php?language=zh_CN"
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/install.php?language=zh_CN", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_data = {"timezone": "Asia/Shanghai", "password": "cuc123", "install": ''}
    requests.post(burp0_url, headers=burp0_headers,  data=burp0_data)

def login(host):
    session = requests.session()
    burp0_url = "http://"+host+"/admin/"
    r=session.get(burp0_url)
    txt=r.text
#print(txt)
    token=re.search('"tokenCSRF" value=\"(.*?)\">', txt, re.DOTALL).group(1)
    print(token)
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/admin/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_data = {"tokenCSRF": token, "username": "admin", "password": "cuc123", "save": ''}
    r=session.post(burp0_url, headers=burp0_headers,  data=burp0_data)
    html_set_cookie = requests.utils.dict_from_cookiejar(session.cookies)
    print(html_set_cookie)
    return html_set_cookie
    #print(r.status_code)

def back(cookies,host):
    burp0_url = "http://"+host+"/admin/install-plugin/pluginBackup"
    burp0_cookies = cookies
    burp0_headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/admin/plugins", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
   

def adduser(cookies,host):   
    burp0_url = "http://"+host+"/admin/new-user"
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/admin/new-user", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_cookies = cookies
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    txt=r.text
#print(txt)
    token=re.search('"tokenCSRF" value=\"(.*?)\">', txt, re.DOTALL).group(1)
    print(token)  
    burp0_data = {"save": '', "tokenCSRF": token, "new_username": "user", "new_password": "123456", "confirm_password": "123456", "role": "author", "email": ''}
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    burp0_data = {"save": '', "tokenCSRF": token, "new_username": "user2", "new_password": "123456", "confirm_password": "123456", "role": "author", "email": ''}
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    burp0_data = {"save": '', "tokenCSRF": token, "new_username": "user3", "new_password": "123456", "confirm_password": "123456", "role": "author", "email": ''}
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    #print(r.text)
    return token 

def title(cookies,token,host):

    burp0_url = "http://"+host+"/admin/settings"
    burp0_cookies = cookies
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/admin/settings", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_data = {"save": '', "tokenCSRF": token, "title": "ChinaMobile", "slogan": "中国移动欢迎你", "description": "主要面向中国移动客户", "footer": "Copyright \xc2\xa9 2020", "itemsPerPage": "6", "orderBy": "date", "emailFrom": "no-reply@"+host+"", "autosaveInterval": "2", "url": "", "markdownParser": "true", "uriPage": "/", "uriTag": "/tag/", "uriCategory": "/category/", "extremeFriendly": "true", "titleFormatHomepage": "{{site-slogan}} | {{site-title}}", "titleFormatPages": "{{page-title}} | {{site-title}}", "titleFormatCategory": "{{category-name}} | {{site-title}}", "titleFormatTag": "{{tag-name}} | {{site-title}}", "twitter": "https://twitter.com/bludit", "facebook": "https://www.facebook.com/bluditcms", "codepen": '', "instagram": '', "gitlab": '', "github": "https://github.com/bludit", "linkedin": '', "mastodon": '', "dribbble": '', "vk": '', "thumbnailWidth": "400", "thumbnailHeight": "400", "thumbnailQuality": "100", "language": "zh_CN", "timezone": "Asia/Shanghai", "locale": "zh_CN", "dateFormat": "F j, Y", "customFields": "[]", "inputFile": ''}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)

def about(cookies,token,host):
  
    burp0_url = "http://"+host+"/admin/configure-plugin/pluginAbout"
    burp0_cookies =cookies
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/admin/configure-plugin/pluginAbout", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_data = {"save": '', "tokenCSRF": token, "label": "关于我们", "text": "全新全意为中国移动客户服务"}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)


def delart(cookies,token,host):
    burp0_url = "http://"+host+"/admin/edit-content/follow-bludit"
    burp0_cookies =cookies
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/admin/content", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    burp0_data = {"tokenCSRF": token, "key": "follow-bludit", "type": "delete"}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)

def addart(cookies,host):
    burp0_url = "http://"+host+"/admin/new-content"
    burp0_cookies =cookies
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/admin/new-content", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    txt=r.text
    uuid=re.search('"uuid" value=\"(.*?)\">', txt, re.DOTALL).group(1)
    token=re.search('"tokenCSRF" value=\"(.*?)\">', txt, re.DOTALL).group(1)
    burp0_data = {"tokenCSRF": token, "uuid": uuid, "type": "published", "coverImage": '', "content": "6月18日上午消息，中国移动5G智慧矿山联盟成立大会暨全国首座5G煤矿落成仪式今日在山西太原举行。会上，中国移动联合清华大学、中国矿业大学（北京）、阳煤集团、中煤科工、华为公司等70多家单位成立“5G智慧矿山联盟”，并宣布在阳煤集团新元煤矿正式落成全国首座5G煤矿。山西省省长林武、常务副省长胡玉亭、中国移动董事长杨杰、副总经理赵大春等出席活动。", "category": '', "description": "", "date": "2020-06-19 21:05:57", "typeSelector": "published", "position": "2", "tags": '', "template": '', "externalCoverImage": '', "slug": "", "noindex": "0", "nofollow": "0", "noarchive": "0", "title": "中移动成立5G智慧矿山联盟"}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)

    burp0_data = {"tokenCSRF": token, "uuid": uuid, "type": "published", "coverImage": '', "content": "6月17日，中国移动“创新2020，云上科技周”在网络云平台正式开幕。中移物联网有限公司总经理乔辉在会上发布了中国移动物联网操作系统——OneOS。", "category": '', "description": "", "date": "2020-06-17 21:05:57", "typeSelector": "published", "position": "2", "tags": '', "template": '', "externalCoverImage": '', "slug": "", "noindex": "0", "nofollow": "0", "noarchive": "0", "title": "面向5G，中国移动发布物联网操作系统OneOS"}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)

    burp0_data = {"tokenCSRF": token, "uuid": uuid, "type": "published", "coverImage": '', "content": "2020年中国移动对5G的大手笔投资是意料之中，毕竟2020年是5G建设的高峰期。从3月6日工信部召开的加快5G发展专题会释放的信息来看，5G基建成为“新基建”中的主要抓手，今年5G网络建设将加速又加量，运营商预计年底前开通60万5G基站。", "category": '', "description": "", "date": "2020-06-13 21:05:57", "typeSelector": "published", "position": "2", "tags": '', "template": '', "externalCoverImage": '', "slug": "", "noindex": "0", "nofollow": "0", "noarchive": "0", "title": "中国移动：1000亿投资30万座5G基站"}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    
    burp0_data = {"tokenCSRF": token, "uuid": uuid, "type": "published", "coverImage": '', "content": "日前，中国移动通信集团副总经理董昕在媒体见面会上透露，中国移动将在2019年5万个5G基站基础上，2020年加快从NSA向SA的目标演进，力争第四季度实现SA商用。董昕表示，中国移动在2019年建设了超过5万个5G基站，在此基础上，今年将围绕建设“覆盖全国、技术先进、品质优良”5G精品网络目标，在全国地级以上城市建设5G网络；深化开放合作促进SA产业成熟，加快从NSA向SA的目标网演进，力争第四季度实现SA商用", "category": '', "description": "", "date": "2020-07-13 21:05:57", "typeSelector": "published", "position": "2", "tags": '', "template": '', "externalCoverImage": '', "slug": "", "noindex": "0", "nofollow": "0", "noarchive": "0", "title": "中国移动：力争2020年四季度实现,SA商用"}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)

    burp0_data = {"tokenCSRF": token, "uuid": uuid, "type": "published", "coverImage": '', "content": "中国信息通信研究院发布了2019年第三季度中国宽带资费水平报告，数据显示，2019年第三季度，我国移动通信月户均支出为47.3元，同比下降9.5%；固定宽带月户均支出为35.8元，同比下降12%。", "category": '', "description": "", "date": "2020-07-13 21:05:57", "typeSelector": "published", "position": "2", "tags": '', "template": '', "externalCoverImage": '', "slug": "", "noindex": "0", "nofollow": "0", "noarchive": "0", "title": "我国移动通信月户均支出47.3元 远低于全球平均水平"}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)


def aboutcon(cookies,token,host):
    burp0_url = "http://"+host+"/admin/edit-content/about"
    burp0_cookies = cookies
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://"+host+"", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://"+host+"/admin/edit-content/about", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    r=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    txt=r.text
    uuid=re.search('"uuid" value=\"(.*?)\">', txt, re.DOTALL).group(1)
    token=re.search('"tokenCSRF" value=\"(.*?)\">', txt, re.DOTALL).group(1)

    burp0_data = {"tokenCSRF": token, "uuid": uuid, "type": "static", "coverImage": '', "content": "<p>中国移动通信集团有限公司（英文名称：China Mobile Communications Group Co.,Ltd，简称“中国移动”、“CMCC”或“中国移动通信”、“中移动”）是按照国家电信体制改革的总体部署，于2000年4月20日成立的中央企业。2017年12月，中国移动通信集团公司进行公司制改制，企业类型由全民所有制企业变更为国有独资公司，并更名为中国移动通信集团有限公司。中国移动是一家基于GSM、TDD-LTE、FDD-LTE制式网络的移动通信运营商。 [1]  中国移动全资拥有中国移动（香港）集团有限公司，由其控股的中国移动有限公司在国内31个省（自治区、直辖市）和香港设立全资子公司，并在香港和纽约上市，主要经营移动语音、数据、宽带、IP电话和多媒体业务，并具有计算机互联网国际联网单位经营权和国际出入口经营权。注册资本3000亿人民币，资产规模近1.7万亿人民币，员工总数近50万人。</p>", "key": "about", "category": "general", "description": '', "date": "2020-07-13 17:55:30", "typeSelector": "static", "position": "1", "tags": '', "template": '', "externalCoverImage": '', "slug": "about", "noindex": "0", "nofollow": "0", "noarchive": "0", "title": "About"}
    requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)



def check(host):
    burp0_url = "http://"+host+""
    r=requests.get(burp0_url)
    result=r.text
    if("ChinaMobile" in result):
        print('Config success!')
        return 0
    else:
        print('Config fail!')
        return -1


if __name__ == "__main__":
    host =sys.argv[1]
    #host= "192.168.56.101:8000"
    setlag(host)
    setadmin(host)
    result=login(host)
    cookies=result
    back(cookies,host)
    token=adduser(cookies,host)
    title(cookies,token,host)
    about(cookies,token,host)
    delart(cookies,token,host)
    addart(cookies,host)
    aboutcon(cookies,token,host)
    check(host)