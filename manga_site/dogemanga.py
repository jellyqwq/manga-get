# coding=utf-8
# 漫画狗
import re
from urllib import parse
from requests_site import requests_site
from manga_save import Manga_save
import random
import time

def dogemanga_get_p(url='', book_folder_name=''):
    content = requests_site(url)
    chapter_title = re.compile(r'<title>(.*?)</title>', re.M|re.S)
    compile_response = re.compile(r'<img .*?>', re.M|re.S)
    compile_name = re.compile(r'alt="(.*?)"', re.M|re.S)
    compile_url = re.compile(r'(?:data-|)src="(.*?)"', re.M|re.S)

    chapter_folder_name = re.findall(chapter_title, content)[0]
    img_tag =  re.findall(compile_response, content)
    li_manga = []
    for i in img_tag:
        if 'site-page-index' in i:
            manga_name = re.findall(compile_name, i)
            manga_url = re.findall(compile_url, i)
            li_manga.append([manga_name[0], manga_url[0]])
        else:
            pass
    save = Manga_save()
    save.manga_save(li_link=li_manga, chapter_folder_name=chapter_folder_name, book_folder_name=book_folder_name)

def dogemanga_get_m(url=''):
    content = requests_site(url)
    # 提取m页的漫画标题作为大的文件夹
    book_title = re.compile(r'<title>(.*?)</title>', re.M|re.S)
    # 提取m页下的select标签内容
    tag_select = re.compile(r'<select id="site-manga-publication-index">(.*?)</select>', re.M|re.S)
    # 提取m页下的每一话的名字和地址
    pages_information = re.compile(r'<option value="(?P<chapter_url>.*?)">(?P<chapter_name>.*?)</option>', re.S|re.M)
    # 将tag_select找到的内容去除换行符
    page_str = re.findall(tag_select, content)[0].replace('\n', '')
    # 大文件夹名字
    book_folder_name = re.findall(book_title, content)[0]
    # 创建一个空列表用于存放每一话的名字和url
    li_page_information = []
    # 通过finditer方法将每一话的名字和url进行遍历输出
    for i in pages_information.finditer(page_str):
        li_page_information.append([i.group('chapter_name'), i.group('chapter_url')])

    li_page_information.reverse()

    for link in li_page_information:
        print('='*50)
        print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()), book_folder_name, f'{link[0]} 准备白嫖')
        dogemanga_get_p(link[1], book_folder_name)
        print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()), book_folder_name, f'{link[0]} 白嫖完成')
        print('='*50)
        time.sleep(random.uniform(1.2,2.1))

def dogemanga_get_q(url=''):
    content = requests_site(url)
    pattern = re.compile(r'<a class="site-red-dot-box site-link" href="(?P<url>.*?)">(?P<manga_name>.*?)<', re.M|re.S)
    li = pattern.finditer(content)
    for i in li:
        dogemanga_get_m(i.group('url'))

# 漫画狗网站主函数
def dogemanga_main(url=''):
    # cop对url进行解析,判断是网页时目录页m还是漫画页p
    cop =  re.compile(r'(?:https|http)://dogemanga.com/(.{1})')
    # copname对url中漫画名字提取
    # copname = re.compile(r'(?:https|http)://dogemanga.com/.*?/(.*?)/')
    # 网页类型m\p\q
    cop = re.findall(cop, url)
    # 漫画名
    # copname = re.findall(copname, url)
    # 对url中的中文字符解码
    # copname = parse.unquote(copname[0])
    if cop[0] == '?':
        dogemanga_get_q(url)
    elif cop[0] == 'm':
        dogemanga_get_m(url)
    elif cop[0] == 'p':
        dogemanga_get_p(url)
    else:
        return None
