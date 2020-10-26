from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

rank = [['Werner','1'],['Henderson','2'],['Sterling','3'],['Davies','4'],
    ['Mane','5'],['Havertz','6'],['Dybala','7'],['Sancho','8'],['Fernandes','9'],['Gnabry','10'],
    ['Ramos','11'],['Haaland','12'],['Muller','13'],['Mbappe','14'],['DeBruyne','15'],['Neymar','16'],['Benzema','17'],
    ['Messi','18'],['Ronaldo','19'],['Lewandowski','20']]

Players = []

for playerAndrank in rank:
    for i in range(int(playerAndrank[1])):
        Players.append(playerAndrank[0])

#print(Players)

player_collect = " ".join(Players)
wordCloudFileName = "2020_UEFA_rank_wordCloud.png"
img_mask = np.array(Image.open('adidas_logo.png'))
wordCloudResult = WordCloud(background_color='white',mask=img_mask,font_path='SoukouMincho.ttf',collocations=False).generate(player_collect)
plt.figure(figsize=(10,5))
plt.imshow(wordCloudResult)
plt.axis("off")
plt.show()
wordCloudResult.to_file(wordCloudFileName)
