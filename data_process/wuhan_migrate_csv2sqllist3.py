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
# cursor = c.execute("SELECT *  from charts_wuhanpopulationmigrationout")

# for row in cursor:
#     print("id = " + str(row[0]) + "year = " + str(row[1]) + "date = " + str(row[2]) + "province = " + row[4])

df = pandas.read_excel('E:/py/excise/wuhan_migrate_out.xls', encoding='utf-8')
df.rename(columns={'城市代码': 'city_code', '迁出目的地': 'city_name'}, inplace=True)
df['city_rate_out'] = df.iloc[:, list(range(2, 178))].mean(axis=1)
df = df.drop(df.iloc[:, list(range(2, 178))], axis=1)
# print(df)

df2 = pandas.read_excel('E:/py/excise/wuhan_migrate_in.xls', encoding='utf-8')
df2.rename(columns={'城市代码': 'city_code', '迁入来源地': 'city_name'}, inplace=True)
df2['city_rate_in'] = df2.iloc[:, list(range(2, 178))].mean(axis=1)
df2 = df2.drop(df2.iloc[:, list(range(2, 178))], axis=1)
# print(df2)
df = df.merge(df2)
df['city_code'] = df['city_code'].astype('int')
for i in range(len(df['city_name'])):
    df['city_name'][i] = df['city_name'][i].strip('市县省')
print(df)

# print(df.columns.values.tolist())
# df.rename(columns={'Unnamed: 0': 'id'}, inplace=True)
# # df.dropna()
# df['confirm_add'] = df['confirm_add'].fillna(0)
# df['confirm_add'] = df['confirm_add'].astype('int')
#
# # print(df[df.isnull().values == True])
# print(df)
df.to_sql('charts_wuhanpopulationmigrationout', conn, if_exists='append', index=False)
print('牛哇')
conn.close()
