import os
from bs4 import BeautifulSoup
import urllib.request as urlRequest
import json


def Prey():
    url = "https://news.yahoo.co.jp/list/?c=computer"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    preyRequest = urlRequest.Request(url, headers=headers)
    preyPage = urlRequest.urlopen(preyRequest).read().decode('utf8')
    beautifulSoupEntity = BeautifulSoup(preyPage, 'html.parser')
    print(beautifulSoupEntity)
    