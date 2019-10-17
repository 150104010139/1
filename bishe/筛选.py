# -*- coding:utf-8 -*-

import re
import jieba
comments=open('testspace.txt', encoding='utf-8')
#comments=open('tfidfspace.txt', encoding='utf-8')

ttt=open('wenben.txt','w+',encoding='utf-8')

for f in comments:
    pattern=re.compile(r'[\u4e00-\u9fa5]+')
    filterdata=re.findall(pattern,f)
    result=' \n'.join(filterdata)
    print(result)
    ttt.write(result)


