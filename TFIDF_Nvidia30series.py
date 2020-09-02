import requests
import pandas as pd
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfTransformer
ptt_list = requests.get('https://www.ptt.cc/bbs/PC_Shopping/M.1599018066.A.29F.html',verify=False)
ptt_soup = BeautifulSoup(ptt_list.text)
title_name = ptt_soup('title')[0].text
for i in ptt_soup.select('.push-content'):
    print(title_name[:-18],',',i.text[1:])
trans_tfidf = TfidfTransformer()
tfidf = trans_tfidf.fit_transform(df_all)
tf_idf = pd.DataFrame(tfidf.toarray()).set_index(df_all.index)