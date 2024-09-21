# Python-WordCloud: 文字雲視覺化應用：新聞關鍵字分析

> 使用者輸入欲搜尋新聞主題，得到 Google 新聞搜尋文字內容，接續使用 Jieba 套件進行斷詞分析，TF-IDF 算法提取關鍵詞，最終生成文字雲。

> 理想目標：擴大文本搜尋範圍，改善斷詞結果，在網頁前端直接生成文字雲，方便分享至社群平台。

To-do:

- [x] 指定日期範圍搜尋新聞
- [x] 使用正則表達式過濾英文
- [x] 使用 tl-idf 篩選關鍵詞
- [x] 調整圖片遮罩增強視覺效果
- [ ] 解決中文新聞日期格式問題
- [ ] [使用 CkipTagger 取代 Jieba](https://github.com/wastu01/Python-WordCloud/issues/1#issue-1028103420)
- [ ] 圖表呈現媒體來源類型

## 文字雲輸出畫面

![疫情關鍵字文字雲](img/2021-05-13-疫情.png)

![新聞關鍵字文字雲](https://raw.githubusercontent.com/wastu01/Python-WordCloud/5a27d021af9e68caee4c0bf5eec68dcae78c5aac/img/20240920_柯文哲_title%2Bdesc_relative_scaling1%25.png)

![柯文哲關鍵字文字雲](https://raw.githubusercontent.com/wastu01/Python-WordCloud/refs/heads/master/img/20240919_%E6%9F%AF%E6%96%87%E5%93%B2_relative_scaling20%25.png)


## 學習資源：

- [自動化新聞搜尋實作](http://13.231.129.69/2020/11/11/python-googlenews/)
- [GoogleNews 套件使用教學](https://clay-atlas.com/blog/2019/10/14/python-chinese-tutorial-googlenews-package/)
- [大數據分析實務-資料分析](https://hackmd.io/@aaronlife/python-bigdata-02)
- [Jieba 與 Gensim 歌詞斷詞分析 / TF-IDF 說明](https://github.com/youngmihuang/lyrics_application)


## 延伸閱讀

中研院中文詞知識庫小組計畫主持人馬偉雲專訪內容

https://aiacademy.tw/what-is-nlp-natural-language-processing/


<!--if you see this, congrats! https://hackmd.io/@DCT/google-news-package-learning-with-gpt -->





