# Author: Peanut
# -*- codeing = utf-8 -*-
# @Time : 2020/8/3 13:12
# @File : wechat.py
# @Software :PyCharm

from selenium import webdriver
from PIL import Image
import pytesseract
import os
import time

wd = webdriver.Chrome(r'F:\edgedriver_win64\msedgedriver.exe')
wd.implicitly_wait(5)
wd.get("https://h5.zhiyyuan.com/m.php?v=c00a0c61261cfa98&id=190&sign=friend&from=groupmessage&id=98&sign=friend")

