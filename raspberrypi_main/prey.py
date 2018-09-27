import os
from bs4 import BeautifulSoup
import urllib.request as urlRequest
import time
import re
import datetime
import lxml
import ssl



def prey():
    ssl._create_default_https_context = ssl._create_unverified_context
    url = "https://news.yahoo.co.jp/list/?c=computer"
    list_save = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    prey_request = urlRequest.Request(url, headers=headers)
    prey_page = urlRequest.urlopen(prey_request).read().decode('utf8')
    beautiful_soup_entity = BeautifulSoup(prey_page, 'lxml')
    list_box_wrap = beautiful_soup_entity.find_all(class_='ListBoxwrap')  # top20
    for x in list_box_wrap:
        list_save.append(str(x.find_all('dt')[0].string))
        list_save.append(str(x.find_all('time')[0].string))
        for x1 in x.find_all('a'):
            list_save.append(str(x1.get('href')))
            list_save.append(get_info(get_url(str(x1.get('href')))))
            list_save.append(" ")
    return list_save


def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    prey_request = urlRequest.Request(url, headers=headers)
    prey_page = urlRequest.urlopen(prey_request).read().decode('utf8')
    beautiful_soup_entity = BeautifulSoup(prey_page, 'lxml')
    news_link = beautiful_soup_entity.find_all(class_='newsLink')
    data = []
    for news in news_link:
        data.append(news.get('onmousedown').replace('this.href=', ''))
    data = str(data)
    data = data.replace('[', '')
    data = data.replace(']', '')
    data = data.replace('\"', '')
    data = data.replace('\'', '')
    return str(data)


def get_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    prey_request = urlRequest.Request(url, headers=headers)
    prey_page = urlRequest.urlopen(prey_request).read().decode('utf8')
    beautiful_soup_entity = BeautifulSoup(prey_page, 'lxml')
    info = beautiful_soup_entity.find_all(class_='ynDetailText yjDirectSLinkTarget')
    info_box = []
    for i in info:
        info_box.append(i.text.strip())
    info_string = ''.join(info_box)
    info_string = str(re.split('\n', info_string))
    info_string = info_string.replace(u'\\u3000', u'')
    info_string = info_string.replace('[', '')
    info_string = info_string.replace(']', '')
    info_string = info_string.replace('\'', '')
    return str(info_string)

def save_file():
    date_time = datetime.datetime.now().strftime('%Y%m%d')
    url = '../save_file/' + date_time + '.txt'
    if (os.path.exists(url)):
        print('true')
        file = open(url, 'a+', encoding='utf-8')
        for x in prey():
            file.write(x + '\n')
            print(x)
        file.close()

        time.sleep(600)
        return True
    else:
        print('false')
        file = open(url, 'w', encoding='utf-8')
        for x in prey():
            file.write(x + '\n')
        file.close()
        time.sleep(200)
        return True
