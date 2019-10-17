# -*- coding:utf-8 -*-
# ! python3
# -*- coding: utf-8 -*-
import os, codecs
import jieba
from collections import Counter
import mysql.connector
mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123",
            database="xiaoshuo"
        )


def get_words(txt):
    seg_list =jieba.cut(txt)
    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    print('常用词频度统计结果')
    for (k, v) in c.most_common(10000):
        print('%s%s %s  %d' % ('  ' * (5 - len(k)), k, '*' * int(v / 3), v))
        mycursor = mydb.cursor()

        sql = "INSERT INTO computer (word, num) VALUES (%s, %s)"
        val = (k, v)
        mycursor.execute(sql, val)
        mydb.commit()  # 数据表内容有更新，必须使用到该语句
    print(mycursor.rowcount, "记录插入成功。")

if __name__ == '__main__':
    with codecs.open('wenben.txt', 'r', 'utf8') as f:
        txt = f.read()
    get_words(txt)