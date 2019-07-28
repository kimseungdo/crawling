from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib.request

searchterm = 'hyundai car'
horizontal = '1280'
vertical = '720'
url = "https://www.google.com/search?q="+searchterm+"&biw=1662&bih=784&tbm=isch&source=lnt&tbs=isz:ex,iszw:"+horizontal+",iszh:"+vertical
'''
SD size 720 576
HD size 1280 720
FULL HD 1920 1080
Quad HD 3840 2160
2K 4K 4096 2160
Horizenal
<input jsname="d7w5xc" class="ktf mini" value="" autocomplete="off" id="kbqVne" type="text">
Virtualize
<input jsname="zPIbne" class="ktf mini" value="" autocomplete="off" id="XOyNzd" type="text">
'''
'''
https://www.google.com/search?q=hyundai+car&biw=1034&bih=708&tbs=imgo:1,isz:ex,iszw:1280,iszh:720&tbm=isch&source=lnt
https://www.google.com/search?q=hyundai+car&tbas=0&biw=1286&bih=784&tbm=isch&source=lnt&tbs=isz:ex,iszw:horizontal,iszh:vertical
https://www.google.com/search?q="+searchterm+"&source=lnms&tbm=isch
https://www.google.com/search?q=hyundai+car&biw=1662&bih=784&tbm=isch&source=lnt&tbs=isz:ex,iszw:1280,iszh:720
'''

browser = webdriver.Chrome(executable_path = r'C:\Users\Ant\Desktop\75\chromedriver.exe')
browser.get(url)

'''
<input class="gLFyf gsfi" maxlength="2048" name="q" type="text" jsaction="paste:puy29d" aria-autocomplete="both"
aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" role="combobox" spellcheck="false"
title="검색" value="" aria-label="검색"
data-ved="0ahUKEwjpgPDgsNXjAhWGHXAKHejtDnkQ39UDCAQ">
'''
#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input
#hdtb-tls 도구
'''
==//*[@id="hdtbMenus"]/div/div[2] xpath
#hdtbMenus > div > div:nth-child(2) css
'''
#isz_ex > div > a 지정 document.querySelector("#hdtbMenus > div > div:nth-child(2)")
#kbqVne 가로 //*[@id="kbqVne"]
#XOyNzd 세로 //*[@id="XOyNzd"]
#isz_ex > div > div > div.Hrg3ab > div.oW2d8b > button 실행버튼
#isz_ex > div > div:nth-child(2) > div.Hrg3ab > div.oW2d8b > button
browser.find_element_by_xpath('//*[@id="hdtb-tls"]').click() #도구 클릭
browser.implicitly_wait(20)

element = browser.find_element_by_class_name('hdtb-mn-cont')
browser.execute_script("#div > div:nth-child(2).click();", element)

#browser.find_element_by_xpath('//*[@id="hdtbMenus"]/div/div[2]').click() #크기선택 클릭
browser.implicitly_wait(10)
browser.find_element_by_xpath('//*[@id="isz_ex"]/div/a').click()#크기지정 클릭
