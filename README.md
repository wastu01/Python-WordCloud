# Python-WordCloud

> 想法：使用者輸入新聞關鍵字，爬取相關文章內容，並使用 Jieba 進行斷詞分析，最終生成文字雲。

> 理想目標是擴大文本搜尋範圍，並能在網頁前端直接渲染文字雲，方便分享至社群平台。目前先取搜尋結果的文字作為斷詞產生文字雲做為練習。

本專案使用到的套件

#### [GoogleNews](https://pypi.org/project/GoogleNews/)
#### [jieba](https://pypi.org/project/jieba/)
#### [wordcloud](https://pypi.org/project/wordcloud/)
#### [matplotlib](https://pypi.org/project/matplotlib/)
#### [PIL](https://pypi.org/project/Pillow/)
#### [pandas](https://pypi.org/project/pandas/)
#### [numpy](https://pypi.org/project/numpy/)
#### [scipy](https://pypi.org/project/scipy/)


。To-do :
- [ ] 指定日期範圍搜尋新聞
- [ ] 停用詞過濾詞彙
- [ ] 圖表呈現媒體來源類型

## 文字雲輸出畫面：

![](/img/2021-05-13-疫情.png)


## 參考資料：

#### [Python GoogleNews 套件](https://pypi.org/project/GoogleNews/)
#### [Python斷詞與文字雲教學課堂講義](http://120.108.221.55/PROFCHWU/dctai/index.php)
#### [E W 的自動化搜尋新聞實作文章](http://13.231.129.69/2020/11/11/python-googlenews/)
#### [Clay 的教學文章 [Python] 使用 GoogleNews 套件輕鬆取得 Google News 新聞資訊](https://clay-atlas.com/blog/2019/10/14/python-chinese-tutorial-googlenews-package/)
#### [Clay 的教學文章 [Python] wordcloud 模組使用 mask 生成特定形狀、顏色](https://clay-atlas.com/blog/2020/04/24/python-cn-package-note-wordcloud-mask-background/)

### Jieba 進階用法 / tf-idf 說明：
#### [YoungMi Huang 的教學文章 以 jieba 與 gensim 探索文本主題：五月天人生無限公司歌詞分析 ( I )](https://github.com/youngmihuang/lyrics_application)

#### 學習筆記
<!-- - [Python GoogleNews 套件使用紀錄](https://hackmd.io/@DCT/google-news-package-learning-with-gpt) -->
- [NUMPY Matplotlib 學習筆記](https://hackmd.io/@DCT/python-numpy-ndarray-learnings)
- [Pandas模組與資料型態 / Series / DataFrame 學習筆記](https://hackmd.io/@DCT/python-pandas-series-dataframe)

2024/09/03 更新：

> 使用 GoogleNews 的 get_news() 目前得到的網址是 Google頁面轉址連結，跳轉後才會得到正確的新聞連結
> 可參考此專案 [SuYenTing/Python-web-crawler](https://github.com/SuYenTing/Python-web-crawler/blob/main/google_real_time_news.py) 解決方式，使用 google-news-url-decoder 模組。
> 使用 GoogleNews 的 search() 實測可以得到真正的網址




