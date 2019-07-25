from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib.request
import multiprocessing

#검색 url생성 searchterm 찾을 이미지
searchterm = 'megadeth'
url = "https://www.google.com/search?q="+searchterm+"&source=lnms&tbm=isch"
# chrom webdriver 사용하여 브라우저를 가져온다.
browser = webdriver.Chrome('./chromedriver_win32-1/chromedriver')
browser.get(url)
# User-Agent를 통해 봇이 아닌 유저정보라는 것을 위해 사용
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
# 이미지 카운터
counter = 0
succounter = 0

#image size HOR//VER
horizontal = 1280
vertical = 720
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

print(os.path)
# 소스코드가 있는 경로에 '검색어' 폴더없으면 생성
if not os.path.exists(searchterm):
    os.mkdir(searchterm)
   
for _ in range(500):
    # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
    browser.execute_script("window.scrollBy(0,10000)")
'''
구글 검색시 이미지탭에서 이미지 태그는 div태그고 rg_meta에 이미지가 놓임
div태그에서 class name이 rg_meta인 것을 찾아온다
'''
for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
    counter = counter + 1
    print ("Total Count:", counter)
    print ("Succsessful Count:", succounter)
    print ("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])
 
    # 이미지 url
    img = json.loads(x.get_attribute('innerHTML'))["ou"]
    # 이미지 확장자
    imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
    
    # 구글 이미지를 읽고 저장한다.
    try:
        req = urllib.request.Request(img, headers= header)
        raw_img = urllib.request.urlopen(img).read()
        File = open(os.path.join(searchterm , searchterm + "_" + str(counter) + "." + imgtype), "wb")
        File.write(raw_img)
        File.close()
        succounter = succounter + 1
        '''
        python3 버전경우 urllib.request고
        python2 일 경우 urllib2임
        '''
    except:
        print ("can't get img")
            
print (succounter, "succes download")
browser.close()
