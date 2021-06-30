# python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：epidemic_analysis -> word_rate.py
@IDE    ：PyCharm
@Author ：Zhou DingJv
@Date   ：2021/6/28 15:12
@Desc   ：
==================================================
"""

import numpy as np
import pandas
import csv
import sqlite3
import jieba
import codecs
from collections import Counter
#
# conn = sqlite3.connect('db.sqlite3')
# c = conn.cursor()

word = []
num = []

with codecs.open('weibo_content.txt', 'r', encoding='utf-8') as f:
    txt = f.read()

seg_list = jieba.cut(txt)
c = Counter()
for x in seg_list:
    if len(x) > 1 and x != '\r\n':
        c[x] += 1
print('常用词频度统计结果')
for (k, v) in c.most_common(50):
    print('%s%s %s  %d' % ('  ' * (5 - len(k)), k, '*' * int(v / 2), v))
    word.append(k)
    num.append(v)
    break

df = pandas.DataFrame({'word': word, 'num': num})
print(df)
# df.to_sql('charts_weibocommentwordrate', conn, if_exists='append', index=False)
# print('牛哇')
# conn.close()
