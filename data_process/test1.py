# python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：epidemic_analysis -> test1.py
@IDE    ：PyCharm
@Author ：Zhou DingJv
@Date   ：2021/6/28 20:36
@Desc   ：
==================================================
"""
import numpy as np
import pandas as pd

data = {
    "Jack": 78,
    "Marry": 96,
    "Tom": 94,
}

data2 = {
    "Jack1": 708,
    "Marry1": 906,
    "Tom1": 904,
}

dic = pd.DataFrame.from_dict(data, orient='index', columns=['num'])
dic = dic.reset_index().rename(columns={'index': 'word'})
dic['kind'] = 1

dic2 = pd.DataFrame.from_dict(data2, orient='index', columns=['num'])
dic2 = dic2.reset_index().rename(columns={'index': 'word'})
dic2['kind'] = 0

df = pd.concat([dic, dic2])
df = df.reset_index()


df = df.drop('index', axis=1)
df = df.reset_index().rename(columns={'index': 'id'})
print(df)


# data3 = {
#     'positive_sum': 3,
#     'middle_sum': 5,
#     'negative_sum': 0,
# }
#
# df1 = pd.DataFrame.from_dict(data3, orient='index').T
# print(df1)