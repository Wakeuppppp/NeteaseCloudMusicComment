# Author: Peanut
# -*- codeing = utf-8 -*-
# @Time : 2020/7/27 13:44
# @File : test.py
# @Software :PyCharm
import urllib.request, urllib.error
from urllib.parse import urlencode
from selenium import webdriver
import re, time
import sqlite3

'''
爬取图片 添加头部信息
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent',
                      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")]
urllib.request.install_opener(opener)
i = 1
urllib.request.urlretrieve('图片或视频的链接地址', r'存储到本地的路径及名称' + str(i) + ".jpg")
'''

'''
处理爬取的链接中的汉字，urlencode操作
code = '島風'
codes = urllib.parse.quote_plus(code)
print(codes)
'''

wd = webdriver.Edge(r'F:\edgedriver_win64\msedgedriver.exe')
wd.implicitly_wait(5)
wd.get('https://music.163.com/#')
srch = wd.find_element_by_id('srch')
srch.send_keys('习惯失恋\n')
wd.switch_to.frame('g_iframe')
time.sleep(2)
wd.find_element_by_css_selector('span.s-fc7').click()
getName = re.sub(' ', '', wd.find_element_by_css_selector('em.f-ff2').text)
getName = re.sub('/', '', getName)
getName = re.sub('\(', '', getName)
getName = re.sub('\)', '', getName)

getComment = wd.find_elements_by_css_selector('div.cntwrap .f-brk')
print(getName)
for comment in getComment:
    print(comment.text)

# sql = '''
#         create table %s(
#             id integer primary key autoincrement,
#             comment text);
#     ''' % getName


# conn = sqlite3.connect('Comment.db')
# cur = conn.cursor()
# cur.execute(sql)
# conn.commit()
# cur.close()
# conn.close()


def main():
    pass







if __name__ == '__main__':
    main()
