#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by yeongsun on 2021/12/19

import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

def getPageString(url):
    data = requests.get(url, headers = headers)
    # print(data.content)
    return data.content