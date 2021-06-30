# python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：py -> csv2sqllist3.py
@IDE    ：PyCharm
@Author ：Zhou DingJv
@Date   ：2021/6/24 8:34
@Desc   ：
==================================================
"""
import numpy as np
import pandas
import csv
import sqlite3

conn = sqlite3.connect('E:/py/excise/db.sqlite3')
c = conn.cursor()
print(c)
# cursor = c.execute("SELECT *  from charts_provincehistoryepidemicdata")
# for row in cursor:
#     print("id = " + str(row[0]) + "year = " + str(row[1]) + "date = " + str(row[2]) + "province = " + row[4])
#

df = pandas.read_csv('F:/province_history_data.csv', encoding='utf-8', dtype={'date': np.str})
df.drop(['country', 'confirm_cuts', 'dead_cuts', 'now_confirm_cuts', 'heal_cuts', 'description', 'wzz', 'wzz_add'], axis=1,
        inplace=True)
print(df.columns.values.tolist())
df.rename(columns={'Unnamed: 0': 'id'}, inplace=True)
# df.dropna()
df['confirm_add'] = df['confirm_add'].fillna(0)
df['confirm_add'] = df['confirm_add'].astype('int')
# print(df[df.isnull().values == True])
print(df)
# df.to_sql('charts_provincehistoryepidemicdata', conn, if_exists='append', index=False)
# print('牛哇')
conn.close()
