from url_analysis import url_analysis
import time
import os, sys

os.chdir(sys.path[0])

def main(url=''):
    start_time = time.time()
    url_analysis(url)
    end_time = time.time()
    print('Process exited after %f seconds' % (end_time-start_time))
    input('请按任意键继续...')
    
if __name__ == '__main__':
    main(url = input('请输入网址:'))
    
