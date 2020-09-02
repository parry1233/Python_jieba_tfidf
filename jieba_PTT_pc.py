import requests
import pandas as pd
import jieba.analyse
from bs4 import BeautifulSoup

req = requests.session()
pc_list = req.get('https://www.ptt.cc/bbs/PC_Shopping/M.1599018066.A.29F.html',verify=False)
pc_soup = BeautifulSoup(pc_list.text)
file_temp=[]
title_name = pc_soup('title')[0].text
print(title_name)
for i in pc_soup.select('.push-content'):
    imp = jieba.analyse.textrank(i.text[1:],topK=3,withWeight=True)
    print(i.text[1:],imp)