#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import jieba
from GoogleNews import GoogleNews
from bs4 import BeautifulSoup
import requests

googlenews = GoogleNews()

googlenews.setlang('cn')
googlenews.setperiod('d')
googlenews.setencode('utf-8')
googlenews.clear()

x = input("請輸入要搜尋的關鍵字，將為你搜集相關字詞內容:")
googlenews.search(x)

# 優化：輸入空白需重新輸入

alldata = googlenews.result()
result = googlenews.gettext()
links = googlenews.get_links()
# print(type(result))
# print(len(result))
# print(alldata)


print()

for n in range(len(result)):
    print(result[n])
    print(links[n])

df = pd.DataFrame(
    {
        '標題': result,
        '連結': links
    })

url = df['連結'][2]
print(url)
# 取其中一篇文章做分析測試

user_agent = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

r = requests.get(url, headers=user_agent)
r.encoding = "utf-8"
web_content = r.text
soup = BeautifulSoup(web_content, 'html.parser')

articleContent = soup.find_all('p')

article = []
for p in articleContent:
    article.append(p.text)

articleAll = '\n'.join(article)

# print(articleAll)
# 分段用


jieba.load_userdict('/Users/larry/Documents/Github/Python-WordCloud/dict.txt.big.txt')

d = articleAll.replace('!', '').replace('／', "").replace('《', '').replace('》', '').replace('，', '').replace('。', '').replace(
    '「', '').replace('」', '').replace('（', '').replace('）', '').replace('！', '').replace('？', '').replace('、',
                                                                                                          '').replace(
    '▲', '').replace('…', '').replace('：', '')
# print(d)

jieba.setLogLevel(10)

# Sentence = jieba.cut(d, cut_all=True)
# print('全模式'+": "  + "/ ".join(Sentence) + '\n')   

# Sentence = jieba.cut(d, cut_all=False)
# print('精確模式'+": " + "/ ".join(Sentence)+ '\n')  

# Sentence = jieba.cut(d)  
# print('Default為精確模式'+": " + "/ ".join(Sentence)+ '\n')

Sentence = jieba.cut_for_search(d)
# print('搜索引擎模式' + ": " + "/ ".join(Sentence) + '\n')


import numpy as np

from PIL import Image

from collections import Counter

import matplotlib.pyplot as plt

from wordcloud import WordCloud, ImageColorGenerator

from scipy.ndimage import gaussian_gradient_magnitude

with open('/Users/larry/Documents/Github/Python-WordCloud/stopword.txt', 'r', encoding="utf-8") as f:
    stopwords = f.read().split('\n')

terms = {}
for sentence in Sentence:
    if sentence in stopwords:
        continue

    if sentence in terms:
        terms[sentence] += 1
    else:
        terms[sentence] = 1

print(Counter(terms))
# generate_from_text()方法會採納stopwords參數 也可使用

# https://coolors.co/palettes/popular


artDf = pd.DataFrame.from_dict(terms, orient='index', columns=['詞頻'])
artDf.sort_values(by=['詞頻'], ascending=False)

img_path = "/Users/larry/Documents/Github/Python-WordCloud/img/color-0.png"

mask_color = np.array(Image.open(img_path))
mask_color = mask_color[::3, ::3]
mask_image = mask_color.copy()
mask_image[mask_image.sum(axis=2) == 0] = 255

edges = np.mean([gaussian_gradient_magnitude(mask_color[:, :, i] / 255., 2) for i in range(3)], axis=0)
mask_image[edges > .08] = 255

wc = WordCloud(font_path="/Users/larry/Library/Fonts/chinese.otf",
               mask=mask_color,
               max_font_size=35,
               max_words=4000,
               stopwords=stopwords,
               margin=0,
               relative_scaling=0)

wc.generate_from_frequencies(terms)
image_colors = ImageColorGenerator(mask_color)
wc.recolor(color_func=image_colors)

# 視覺化

plt.imshow(wc, interpolation="bilinear")
plt.axis("ttf")
plt.figure(figsize=(20, 20))
plt.show()

# plt.savefig("Wordcloud.png")
wc.to_file("img/AI.png")
# 檔名可優化偵測當下日期 使用者輸入字詞 就不用手動更改
