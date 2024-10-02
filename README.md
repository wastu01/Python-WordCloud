# Python-WordCloud: 文字雲視覺化應用：新聞關鍵字分析

> 使用者輸入欲搜尋新聞主題，得到 Google 新聞搜尋文字內容，接續使用 Jieba 套件進行斷詞分析，TF-IDF 算法提取關鍵詞，最終生成文字雲。

> 理想目標：擴大文本搜尋範圍，改善斷詞結果，在網頁前端直接生成文字雲，方便分享至社群平台。

To-do:

- [x] 指定日期範圍搜尋新聞
- [x] 使用正則表達式過濾英文
- [x] 使用 tl-idf 篩選關鍵詞
- [x] 調整圖片遮罩增強視覺效果
- [x] [使用 CkipTagger 取代 Jieba](https://github.com/wastu01/Python-WordCloud/issues/1#issue-1028103420)
- [ ] 解決中文新聞日期格式問題
- [ ] 圖表呈現媒體來源類型

## 文字雲輸出畫面

![疫情關鍵字文字雲](img/2021-05-13-疫情.png)

![新聞關鍵字文字雲](https://raw.githubusercontent.com/wastu01/Python-WordCloud/5a27d021af9e68caee4c0bf5eec68dcae78c5aac/img/20240920_柯文哲_title%2Bdesc_relative_scaling1%25.png)

![柯文哲關鍵字文字雲](https://raw.githubusercontent.com/wastu01/Python-WordCloud/refs/heads/master/img/20240919_%E6%9F%AF%E6%96%87%E5%93%B2_relative_scaling20%25.png)


## 參考資料：

- [自動化新聞搜尋實作](http://13.231.129.69/2020/11/11/python-googlenews/)
- [GoogleNews 套件使用教學](https://clay-atlas.com/blog/2019/10/14/python-chinese-tutorial-googlenews-package/)
- [大數據分析實務-資料分析](https://hackmd.io/@aaronlife/python-bigdata-02)
- [Jieba 與 Gensim 歌詞斷詞分析 / TF-IDF 說明](https://github.com/youngmihuang/lyrics_application)
- [CKIP 中文斷詞模型使用範例 使用到 double zip  / extend / pandas apply /](https://medium.com/tkustatdc/nlp-自然語言處理-02-文本前處理-ckip中文斷詞-e7db5c147bef)
- [CKIP Transformers documents](https://ckip-transformers.readthedocs.io/en/stable/main/readme.html)
- [簡單好學的中文LDA(Latent Dirichlet Allocation)主題分類模型](https://medium.com/@hjeremy1222/簡單好學的中文lda-latent-dirichlet-allocation-主題分類模型-b0a0d2435b60)

## 延伸閱讀

中研院中文詞知識庫小組計畫主持人馬偉雲專訪內容
https://aiacademy.tw/what-is-nlp-natural-language-processing/

中央研究院詞庫小組聊天機器人應用
https://ckip.iis.sinica.edu.tw/project/chatq/

文理組人都能上手的入門 NLP（自然語言處理） 鐵人賽系列
https://ithelp.ithome.com.tw/articles/10295726


## 檔案內容

Googlenews_bs4.ipynb : 嘗試解析 Google Search 的版本

Googlenews_test.ipynb : GoogleNews 套件語法測試，資料轉換，資料呈現方式規劃

Googlenews_v1.py : 原始構想版本

Googlenews_v2.ipynb : 基於原始版本進行修改

1. Jienba / Ckip transformer 斷詞模型比較
2. 正則表達式篩選字詞，Counter 統計字數
3. Pandas Series / DataFrame 資料排序轉換
4. 從網頁獲取顏色清單 ( 使用 Javascript )
5. 自定義圖片遮罩，產生棋盤形狀圖片遮罩 
6. Pillow Numpy 圖片去躁，邊緣檢測
(邊緣檢測的方式偏難懂，有使用 AI 輔助開發解惑)

## 其他想法：

1. 使用者輸入"時事"，從 Google Trends RSS 得到資料，分析時事產出文字雲。
2. 使用著輸入"焦點"，從 Google News RSS 得到焦點新聞，分析時事產出文字雲。
3. 搭配 Google Search 查詢相關主題，加大文本資料。
4. 斷詞後能否評估此文章為正向還是負向情緒？

<!--if you see this, congrats! https://hackmd.io/@DCT/google-news-package-learning-with-gpt -->