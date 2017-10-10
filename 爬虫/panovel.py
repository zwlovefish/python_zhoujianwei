# -*-coding:utf-8 -*-
# Author:周健伟
#获取小说网页
import requests
from bs4 import BeautifulSoup
import os
#得到页面的html的text文件，方便使用BeautifulSoup插件解析
def get_html(url):
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'
    }
    page=requests.get(url,headers=header)
    page.encoding='gbk'
    return page.text
#使用beautifulsoup插件解析html文件并得到我想要的章节的标题和内容
def jixi_html(html):
    soup=BeautifulSoup(html,'lxml')
    content=soup.find_all("div",id="content")#得到内容
    content.append(soup.find("h1"))#得到标题
    return content
#下载url里的这一章小说的内容和标题
def down_character(url,novel_title):
    character_txt=get_html(url)
    content=jixi_html(character_txt)
    title=content.pop().get_text()#使用get_text()方法可以得到标签里的内容，而去除掉标签
    title="\t\t\t\t"+title+'\t\t\t\t\t\n'
    content_data=content[0].get_text()#一开始将标题pop（）出去，现在这个列表里只剩下了小说内容
    os.chdir('f:/ebooks')#将下载的目录转移到F:/ebooks中
    with open(novel_title,'a',encoding='utf-8') as f:
        f.write(title)
        f.write(content_data)
        f.write('\n')
#爬每个章节小说的地址
def get_character_total(url):
    try:
        urllist=[]
        character_total_txt=get_html(url)
        soup=BeautifulSoup(character_total_txt,'lxml')
        character_div=soup.find_all('dd')[9:]#撇除一开始最新的几章，从第一章开始下载
        for eachitem in character_div:
            urllist.append(eachitem.a['href'])
        urllist.append(soup.find('h1').get_text())
    except:
        pass
    finally:
        return urllist
def main():
    url_character_total = input("小说全部章节的地址是：").strip()
    character_urllist=get_character_total(url_character_total)
    novel_title=character_urllist.pop()+'.txt'
    print(novel_title)
    url="http://www.booktxt.net"
    for eachurl in character_urllist:
        try:
            downurl=url+eachurl
            print("正在下载"+downurl)
            down_character(downurl,novel_title)
        except:
            print("下载发生了异常")
main()