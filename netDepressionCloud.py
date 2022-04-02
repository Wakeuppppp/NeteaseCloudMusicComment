# Author: Peanut
# -*- codeing = utf-8 -*-
# @Time : 2020/7/28 9:51
# @File : netDepressionCloud.py
# @Software :PyCharm

from selenium import webdriver
import re
import sqlite3


def getView(mUrl):
    wd = webdriver.Edge(r'F:\edgedriver_win64\msedgedriver.exe')
    wd.implicitly_wait(5)
    wd.get(mUrl)
    wd.switch_to.frame('g_iframe')
    comment = wd.find_elements_by_css_selector('div.cntwrap .cnt')
    commentList = []
    for x in comment:
        i = 0
        temp = x.text
        for y in temp:
            if y == "：" or y == ":":
                i += 1
                temp = temp[i:]
                temp = re.sub('\n', ' ', temp)
                commentList.append(temp)
                break
            else:
                i += 1
    saveView(commentList)
    print('第1页已完成')

    for z in range(2, 12597):
        pages = z
        commentList = []
        if z > 6:
            z = 6
        page = 'a.zpg' + str(z)
        elements = wd.find_element_by_css_selector(page)
        elements.send_keys("\n")

        comment = wd.find_elements_by_css_selector('div.cntwrap .cnt')

        for x in comment:
            i = 0
            temp = x.text
            for y in temp:
                if y == "：" or y == ":":
                    i += 1
                    temp = temp[i:]
                    temp = re.sub('\n', ' ', temp)
                    commentList.append(temp)
                    break
                else:
                    i += 1
        saveView(commentList)
        print('第%d页已完成' % pages)
    wd.quit()


def saveView(commentList):
    dbPath = "Comment.db"
    conn = sqlite3.connect(dbPath)
    cur = conn.cursor()
    # 初始化数据库自增id
    # dele = '''DELETE FROM sqlite_sequence;'''
    # cur.execute(dele)
    for reviews in commentList:
        sql = '''
                insert into musicView (comment) values('%s'); 
            ''' % reviews
        try:
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
            print(reviews)
    cur.close()
    conn.close()


def init_db(dbPath):
    sql = '''
        create table musicView(
            id integer primary key autoincrement,
            comment text);
    '''
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def main():
    dbPath = "Comment.db"
    init_db(dbPath)
    mUrl = 'https://music.163.com/#/song?id=28907016'
    getView(mUrl)


if __name__ == '__main__':
    main()
