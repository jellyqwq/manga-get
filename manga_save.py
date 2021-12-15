import requests
import random
import time
import os

class Manga_save:
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
    
    def manga_save_path(self, book_folder_name='', chapter_folder_name=''):
        
        if book_folder_name == '':
            path = './manga_download/' + chapter_folder_name + '/'
            os.makedirs(path, exist_ok=True)
            exist_file =  os.listdir(path)
            return [exist_file, path]
        
        elif book_folder_name != '':
            path = './manga_download/' + book_folder_name + '/' + chapter_folder_name + '/'
            os.makedirs(path, exist_ok=True)
            exist_file =  os.listdir(path)
            return [exist_file, path]
        
        else:
            pass
        
    def manga_save(self, li_link=None, book_folder_name=None, chapter_folder_name=None, manga_save_format='.jpg'):
        exist_file = self.manga_save_path(book_folder_name=book_folder_name, chapter_folder_name=chapter_folder_name)
        # 下载列表的格式为[漫画每一话名字,url]
        for i in li_link:
            try:
                if (i[0]+manga_save_format) not in exist_file[0]:
                    r = requests.get(url=i[1], headers=self.headers, timeout=10)
                    picture_name = i[0]
                    with open(exist_file[1] + picture_name + manga_save_format, 'wb') as f:
                        f.write(r.content)
                    print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()), picture_name, '\t', '白嫖成功')
                    time.sleep(random.uniform(0.1,1))
                else:
                    print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()), i[0], '\t', '已存在')
            except:
                continue