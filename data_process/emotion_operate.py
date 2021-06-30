from snownlp import SnowNLP
import sqlite3
import pandas as pd

positive_sum = 0
middle_sum = 0
negative_sum = 0

word_positive_list = {}
word_middle_list = {}
word_negative_list = {}

for line in open('weibo_content.txt', 'r', encoding='utf-8').readlines():
    s = SnowNLP(line.strip('\n'))
    if s.sentiments < 0.33:
        emotion = '消极'
        negative_sum += 1
        for word in s.keywords(10):
            if word in word_negative_list:
                word_negative_list[word] += line.count(word)
            else:
                word_negative_list[word] = line.count(word)
    elif s.sentiments < 0.66:
        emotion = '中性'
        middle_sum += 1
        for word in s.keywords(10):
            if word in word_middle_list:
                word_middle_list[word] += line.count(word)
            else:
                word_middle_list[word] = line.count(word)
    else:
        emotion = '积极'
        positive_sum += 1
        for word in s.keywords(10):
            if word in word_positive_list:
                word_positive_list[word] += line.count(word)
            else:
                word_positive_list[word] = line.count(word)

# print(word_positive_list)
# print(word_negative_list)
# print(word_middle_list)
#
# print('积极 = ' + str(positive_sum))
# print('消极 = ' + str(negative_sum))
# print('中性 = ' + str(middle_sum))

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

df1 = pd.DataFrame.from_dict({
    'positive_sum': positive_sum,
    'middle_sum': middle_sum,
    'negative_sum': negative_sum,
}, orient='index').T.reset_index().rename(columns={'index': 'id'})
print(df1)
df1.to_sql('charts_emotiondata', conn, if_exists='append', index=False)
print('牛哇哇哇哇哇')

df_1 = pd.DataFrame.from_dict(word_positive_list, orient='index', columns=['num'])
df_1 = df_1.reset_index().rename(columns={'index': 'word'})
df_1['kind'] = 1

df_2 = pd.DataFrame.from_dict(word_middle_list, orient='index', columns=['num'])
df_2 = df_2.reset_index().rename(columns={'index': 'word'})
df_2['kind'] = 0

df_3 = pd.DataFrame.from_dict(word_negative_list, orient='index', columns=['num'])
df_3 = df_3.reset_index().rename(columns={'index': 'word'})
df_3['kind'] = -1

df_sum = pd.concat([df_1, df_2, df_3])
df_sum = df_sum.reset_index()

df_sum = df_sum.drop('index', axis=1).reset_index().rename(columns={'index': 'id'})
print(df_sum)
df_sum.to_sql('charts_emotionworddata', conn, if_exists='append', index=False)
print('猪哇哇哇哇哇')
conn.close()
