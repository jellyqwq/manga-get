# coding=utf-8
# 漫画狗
import re
from urllib import parse
from requests_site import requests_site
from manga_save import manga_save
import random
import time

def dogemanga_get_p(content=None):
    title = re.compile(r'<title>(.*?)</title>', re.M|re.S)
    compile_response = re.compile(r'<img .*?>', re.M|re.S)
    compile_name = re.compile(r'alt="(.*?)"', re.M|re.S)
    compile_url = re.compile(r'(?:data-|)src="(.*?)"', re.M|re.S)

    folder_name = re.findall(title, content)[0]
    img_tag =  re.findall(compile_response, content)
    manga_li = []
    for i in img_tag:
        if 'site-page-index' in i:
            manga_name = re.findall(compile_name, i)
            manga_url = re.findall(compile_url, i)
            manga_li.append([manga_name[0], manga_url[0]])
        else:
            pass
    manga_save(manga_li, folder_name)

def dogemanga_get_m(content=None):
    tag_select = re.compile(r'<select id="site-manga-publication-index">(.*?)</select>', re.M|re.S)
    pages_information = re.compile(r'<option value="(?P<page_url>.*?)">(?P<page_name>.*?)</option>', re.S|re.M)
    
    page_str = re.findall(tag_select, content)[0].replace('\n', '')

    li_page_information = []
    for i in pages_information.finditer(page_str):
        li_page_information.append([i.group('page_name'), i.group('page_url')])
    return li_page_information

# 漫画狗网站主函数
def dogemanga_main(url=None):
    # cop对url进行解析,判断是网页时目录页m还是漫画页p
    cop =  re.compile(r'(?:https|http)://dogemanga.com/(.*?)/')
    # copname对url中漫画名字提取
    copname = re.compile(r'(?:https|http)://dogemanga.com/.*?/(.*?)/')
    # 网页类型m\p
    cop = re.findall(cop, url)
    # 漫画名
    copname = re.findall(copname, url)
    # 对url中的中文字符解码
    copname = parse.unquote(copname[0])
    if cop[0] == 'm':
        for link in dogemanga_get_m(requests_site(url)):
            # print(link)
            dogemanga_get_p(requests_site(link[1]))
            time.sleep(random.uniform(1.2,2.1))
    elif cop[0] == 'p':
        dogemanga_get_p(requests_site(url))
    else:
        return None