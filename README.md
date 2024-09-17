# Python-WordCloud

> 使用者輸入新聞關鍵字，得到 Google 新聞搜尋結果，使用 Jieba 進行斷詞分析，最終生成文字雲。

> 理想目標：擴大文本搜尋範圍，改善斷詞結果，在網頁前端直接渲染文字雲，方便分享至社群平台。

(2024/09/17更新)

- `get_news()` 函數目前返回的是 Google 頁面轉址連結
- 參考 [SuYenTing/Python-web-crawler](https://github.com/SuYenTing/Python-web-crawler/blob/main/google_real_time_news.py) 專案，使用 google-news-url-decoder 模組解決轉址問題
- `search()` 函數可以獲取真正的新聞網址
- 非英文語言搜尋時，無法返回正確的 datetime 時間格式


To-do:

- [x] 指定日期範圍搜尋新聞
- [ ] 停用詞過濾詞彙
- [ ] 圖表呈現媒體來源類型

## 本專案使用的套件

- [GoogleNews](https://pypi.org/project/GoogleNews/)
- [jieba](https://pypi.org/project/jieba/)
- [wordcloud](https://pypi.org/project/wordcloud/)
- [matplotlib](https://pypi.org/project/matplotlib/)
- [PIL](https://pypi.org/project/Pillow/)
- [pandas](https://pypi.org/project/pandas/)
- [numpy](https://pypi.org/project/numpy/)
- [scipy](https://pypi.org/project/scipy/)


## 文字雲輸出畫面

![疫情相關文字雲](/img/2021-05-13-疫情.png)


## 參考資料：

#### [Python GoogleNews 套件](https://pypi.org/project/GoogleNews/)
#### [Python斷詞與文字雲教學課堂講義](http://120.108.221.55/PROFCHWU/dctai/index.php)
#### [E W 的自動化搜尋新聞實作文章](http://13.231.129.69/2020/11/11/python-googlenews/)
#### [Clay 的教學文章 [Python] 使用 GoogleNews 套件輕鬆取得 Google News 新聞資訊](https://clay-atlas.com/blog/2019/10/14/python-chinese-tutorial-googlenews-package/)
#### [@aaronlife 第二堂課：大數據分析實務-資料分析](https://hackmd.io/@aaronlife/python-bigdata-02)

### Jieba 進階用法 / tf-idf 說明：
#### [YoungMi Huang 的教學文章 以 jieba 與 gensim 探索文本主題：五月天人生無限公司歌詞分析 ( I )](https://github.com/youngmihuang/lyrics_application)

延伸閱讀
中研院中文詞知識庫小組計畫主持人馬偉雲專訪內容
https://aiacademy.tw/what-is-nlp-natural-language-processing/

<!--if you see this, congrats! https://hackmd.io/@DCT/google-news-package-learning-with-gpt -->





