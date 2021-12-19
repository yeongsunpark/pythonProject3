#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by yeongsun on 2021/12/19

from stringgetter import getPageString
from bs4 import BeautifulSoup

# <태그명 속성="속성값">... </태그명>
# 태그 이름만 특정 soup.find('태그명')
# 태그 속성만 특정 soup.find(속성='속성값') soup.find(attrs = {'속성':'속성값'})
# 태그 이름과 속성 모두 특정 soup.find('태그명', 속성='속성값')


def getProducts_coupang(string):
    bsObj = BeautifulSoup(string, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})  #아이템 리스트부분 추출
    lis = ul.findAll("li", {"class":"baby-product renew-badge"}) #각 아이템 추출

    for item in lis:
        #url
        a = item.find("a", {"class": "baby-product-link"})
        url = a.get('href')
        # print("url:", url)

        #name
        div_name = item.find("div", {"class":"name"})
        name = div_name.getText()
        print("name:", name.strip())

        #image
        dt_image = item.find("dt", {"class":"image"})
        image = dt_image.find("img").get('src')
        # print("image:", image)

        #price
        price = item.find("strong", {"class":"price-value"}).getText()
        print("price:", price.strip())

        # base-price
        try:
            base_price = item.find("del", {"class":"base-price"}).getText()
        except:
            base_price = price
        print("base-price:", base_price.strip())
    print(len(lis))



def getProducts_ssg(string):
    bsObj = BeautifulSoup(string, "html.parser")
    ul = bsObj.find("div", {"class":"tmpl_itemlist"})  #아이템 리스트부분 추출
    lis = ul.findAll("li", {"class":"cunit_t232"}) #각 아이템 추출

    for item in lis:
        # print (item)
        # exit(1)

        #url
        # a = item.find("a", {"class": "baby-product-link"})
        # url = a.get('href')
        # print("url:", url)

        #name
        div_name = item.find("em", {"class":"tx_ko"})
        name = div_name.getText()
        print("name:", name.strip())

        """
        #image
        dt_image = item.find("dt", {"class":"image"})
        image = dt_image.find("img").get('src')
        # print("image:", image)

        #price
        price = item.find("strong", {"class":"price-value"}).getText()
        print("price:", price.strip())

        # base-price
        try:
            base_price = item.find("del", {"class":"base-price"}).getText()
        except:
            base_price = price
        print("base-price:", base_price.strip())
        """
    print(len(lis))


if __name__ == "__main__":
    url = "http://www.ssg.com/service/emart/dvstore/category.ssg?dispCtgId=6000095739"
    pageString = getPageString(url)
    getProducts_ssg(pageString)