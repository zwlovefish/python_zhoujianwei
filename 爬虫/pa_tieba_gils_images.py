# -*-coding:utf-8 -*-
# Author:周健伟
import urllib.request
import os
from bs4 import BeautifulSoup
def get_image_url(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    Soup=BeautifulSoup(html,'html.parser')
    imgpathlist=Soup.findAll('img',class_='BDE_Image')
    impathList=[]
    for eachitem in imgpathlist:
        impathList.append(eachitem['src'])
    return impathList
def down_load_images(filename,url):
    try:
        f=open(filename,'wb')
        data=urllib.request.urlopen(url).read()
        f.write(data)
    except IOError as err:
        print("文件打开失败")
    finally:
        f.close()

count=0
def main():
    url=input("请输入你要爬的帖子的地址")
    ImgPathList=get_image_url(url)
    os.chdir('f:/images')
    for each_url in ImgPathList:
        print("正在下载"+each_url)
        global count
        filename="images1"+str(count)+".jpg"
        down_load_images(filename,each_url)
        count += 1

main()