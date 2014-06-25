# encoding:utf-8
#! /usr/bin/python
__author__ = 'liutianyuan'
"""
using for crawl for certain topics in bbs
"""

import requests
import datetime
import smtplib
import re
import sys
from email.mime.text import MIMEText

reload(sys)
sys.setdefaultencoding('utf-8')


username = 'ltyandy'
password = '295310'
keywords = [u'新闻', u'媒体', u'记者', 'reporter', 'newspaper', 'magazine']
mail_user = '18801733968'
mail_password = 'lty295310'
mail_host = 'smtp.163.com:25'
to_list = ('10300220067@fudan.edu.cn', '77500427@qq.com')


def login_bbs(username, password):
    params = {
        'id': username,
        'pw': password,
    }
    url = 'http://bbs.fudan.edu.cn/bbs/login'

    response = requests.post(url, params, allow_redirects = False)  # get cookies or dead!
    if not response.cookies:
       raise Exception('Can not login!')
    return response.cookies

def search_topic(keyword, time_range, cookies):
    search_url = 'http://bbs.fudan.edu.cn/bbs/bfind'
    keyword = keyword.encode('gb2312')
    params = {'bid': 40,
              't1': keyword,
              'limit': time_range,
              }

    try:
        response = requests.get(search_url, params=params, cookies=cookies)
    except Exception, e:
        print e
        return []
    search_result = response.text

    results = re.findall(r"<po .* id='(?P<id>.*)'>", search_result)

    return results and [int(id) for id in results] or []

def query_detail(id, cookies):
    url = 'http://bbs.fudan.edu.cn/bbs/con?new=1&bid=40&f=' + str(id)
    try:
        response = requests.get(url, cookies=cookies)
    except Exception, e:
        print e
        return False

    text = response.text
    #print text
    result = {}
    title = re.search(r"<title>(.*)</title>", text)
    result['title'] = title.group(1)

    date = re.search(r"<date>(?P<date>.*)</date>", text)
    result['date'] = date.group(1)

    content_raw = re.search(r"<pa m='t'>(.*)</pa>", text)
    content_raw = content_raw.group(1)
    content = clean(content_raw)
    content_real = re.findall(r'<p>(.*?)</p>', content)
    result['content'] = '\n'.join([str(x) for x in content_real])

    return result

def clean(content_raw):
    content = re.sub(r'<br/>','\n',content_raw)
    content = re.sub(r'&#160;',' ', content)
    content = re.sub(r'<c.*/c>','',content)
    return content

def send_mail(to_list, sub, content):
    me = mail_user + '@' + '163.com'
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ';'.join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_password)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
    except Exception, e:
        print e

    return True

def main():
    cookies = login_bbs(username, password)

    for keyword in keywords:
        ids = search_topic(keyword, 1, cookies)
        if ids:
            for id in ids:
                result = query_detail(id, cookies)
                content = result['date'] + '\n' + result['content']
                send_mail(to_list, result['title'], content)
                print 'Sending successfully %s !\n' % str(id)

if __name__ == '__main__':
    main()
