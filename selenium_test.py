#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by yeongsun on 2021/12/19

import pandas as pd
from selenium import webdriver
import time
import math
from bs4 import BeautifulSoup

def getProducts_coupang(req):
    bsObj = BeautifulSoup(req, 'html.parser')
    ul = bsObj.find("div", {"class": "tmpl_itemlist"})  # 아이템 리스트부분 추출
    lis = ul.findAll("li", {"class": "cunit_t232"})  # 각 아이템 추출
    for item in lis:
        div_name = item.find("em", {"class": "tx_ko"})
        name = div_name.getText()
        print("name:", name.strip())


# url = "https://www.coupang.com/np/categories/393760"
url = "http://www.ssg.com/service/emart/dvstore.ssg"
interval = 2
data_list = []
driver = webdriver.Chrome("./chromedriver")
driver.get(url)
time.sleep(interval)
# driver.find_element_by_xpath('//*[@id="searchCategoryComponent"]/ul/li[1]/label').click()
# a = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/ul/li[1]/a/span').click()
driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/ul/li[1]/a/span').click()
# driver.get(a.get_attribute('href'))
req = driver.page_source
getProducts_coupang(req)

driver.find_element_by_xpath('//*[@id="area_itemlist"]/div[2]/a').click()
time.sleep(interval)
req = driver.page_source
getProducts_coupang(req)