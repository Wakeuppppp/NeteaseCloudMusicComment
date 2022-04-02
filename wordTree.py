# Author: Peanut
# -*- codeing = utf-8 -*-
# @Time : 2020/7/7 10:13
# @File : test.py
# @Software :PyCharm

import sqlite3
import jieba
from wordcloud import WordCloud
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np


def wordCloud():
    conn = sqlite3.connect('Comment.db')
    cur = conn.cursor()
    sql = '''select comment from musicView;'''
    text = ''
    datas = cur.execute(sql)
    for data in datas:
        text = text + str(data)
    cur.close()
    conn.close()

    cut = jieba.cut(text)
    string = ' '.join(cut)

    img = Image.open(r'tree.png')
    img_array = np.array(img)
    wc = WordCloud(
        background_color='white',
        mask=img_array,
        font_path='msyh.ttc'
    )
    wc.generate_from_text(string)
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')
    plt.savefig(r'wordTree.jpg', dpi=800)


def main():
    wordCloud()


if __name__ == '__main__':
    main()
