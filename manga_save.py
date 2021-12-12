import requests
import random
import time
import os

def manga_save(li_link=None, folder_name=None):
    os.makedirs('./manga_download/' + folder_name + '/', exist_ok=True)
    exist_file =  os.listdir('./manga_download/'+ folder_name)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    # 下载列表的格式为[漫画每一话名字,url]
    for i in li_link:
        try:
            if (i[0]+'.jpg') not in exist_file:
                r = requests.get(url=i[1], headers=headers, timeout=10)
                picture_name = i[0]
                with open('./manga_download/' + folder_name + '/' + picture_name + '.jpg', 'wb') as f:
                    f.write(r.content)
                print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()), picture_name, '\t', '白嫖成功')
                time.sleep(random.uniform(0.1,1))
            else:
                pass
        except:
            continue