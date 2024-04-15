#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import jieba
from GoogleNews import GoogleNews
from collections import Counter
import matplotlib.pyplot as plt
from datetime import datetime
from PIL import Image
import numpy as np
from scipy.ndimage import gaussian_gradient_magnitude
from wordcloud import WordCloud, ImageColorGenerator

def main():
    # Google News初始化設定
    googlenews = GoogleNews()
    googlenews.setlang('zh-tw')
    googlenews.setperiod('d')
    
    # 使用者輸入關鍵字
    keyword = "藍白"
    # keyword = input("請輸入要搜尋的關鍵字: ")
    googlenews.search(keyword)

    # 獲取搜尋結果
    result = googlenews.result()

    # 顯示新聞標題和連結
    for item in result:
        print(f"標題: {item['title']}")
        print(f"連結: {item['link']}")
        print('---')

    # 進行斷詞處理並計算詞頻
    all_titles = ' '.join([item['title'] for item in result])
    words = jieba.cut(all_titles)
    word_count = Counter(words)

    # 顯示斷詞統計表格
    df = pd.DataFrame(word_count.items(), columns=['word', 'count'])
    df_sorted = df.sort_values(by='count', ascending=False).reset_index(drop=True)
    print(df_sorted.head(20))  # 顯示前20個最常出現的詞
    
        
    # 詢問使用者字體檔案路徑
    font_path_input = "/Users/larry/Github/Python-WordCloud/TaipeiSansTCBeta-Bold.ttf"
    # font_path_input = input("請輸入中文字體的檔案路徑: ")
    # 文字雲圖片遮罩檔案路徑
    img_path = "/Users/larry/Github/Python-WordCloud/img/color-mask.jpeg"
    
    
    mask_color = np.array(Image.open(img_path))
    # 每隔_個像素取一個像素
    mask_color = mask_color[::2, ::2]
    
    mask_image = mask_color.copy()
    threshold = 1  # 根據圖片調整閾值
    mask_image[np.all(mask_image < threshold, axis=2)] = 255
    # 邊緣檢測
    edges = np.mean([gaussian_gradient_magnitude(mask_color[:, :, i] / 255., 2) for i in range(3)], axis=0)
    mask_image[edges > .09] = 255
    
    # 顏色生成
    image_colors = ImageColorGenerator(mask_image)
    image_colors.default_color = [0.9,0.9,0.9]

    # 生成文字雲
    wordcloud = WordCloud(
    font_path=font_path_input,
    width=3200,
    height=1600,
    max_font_size=50,  
    max_words=4000,
    mask=mask_image,
    color_func=image_colors # 從遮罩圖片中提取顏色
    ).generate_from_frequencies(word_count)
    
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


    # 儲存文字雲圖片
    today = datetime.now().strftime('%Y%m%d_%H%M')
    image_filename = f"{today}_{keyword}.png"
    wordcloud.to_file(image_filename)
    print(f"文字雲圖片已儲存為: {image_filename}")

if __name__ == "__main__":
    main()
