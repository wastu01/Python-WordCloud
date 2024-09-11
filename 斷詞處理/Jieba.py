# Jieba github
# https://github.com/fxsjy/jieba?tab=readme-ov-file

# @aaronlife 第二堂課：大數據分析實務-資料分析
# https://hackmd.io/@aaronlife/python-bigdata-02

# NLP
# PPT
# https://drive.google.com/drive/folders/1MoC3e_zf_nwMVtzWdDRPq_RqzI7q16Xe

# 範例程式
# https://colab.research.google.com/drive/1sLy3HbnkW8_Yc85FGRcr0VfgtckZIR7h#scrollTo=GhmNnyMRh5dV

# 什麼是 NLP
# https://aiacademy.tw/what-is-nlp-natural-language-processing/
# 自然語言處理（ Natural Language Processing 簡稱 NLP）


# 匯入 jieba 模組
import jieba
# 載入分析工具
import jieba.analyse

# 自訂繁體中文詞典
WORDS_PATH = r'/Users/larry/Github/Python-WordCloud/dict.txt.big.txt' 
jieba.set_dictionary(WORDS_PATH)

# 自訂專有名詞詞典
# jieba.load_userdict(r'/Users/larry/Github/Python-WordCloud/專有名詞.txt')

# 讀取停用詞
with open(r'../stopword.txt', 'r', encoding='utf-8') as file:
    stopword = file.read().splitlines() # BIF splitlines
    # print(stopword)

# 輸入資料
sentence = '我來自台灣，我畢業於台灣台中教育大學數位內容科技學系，目前正在研究自然語言處理，以及生成式AI工具，請多多指教'

# 調整詞頻
# jieba.suggest_freq('台灣', True)

# 精確模式
seg_list = jieba.cut(sentence, cut_all=False)
print('精確模式: ' + '/'.join(seg_list))

seg_list = jieba.lcut(sentence)
print(f"List 資料型態 :  {seg_list}")

# 全模式
seg_list = jieba.cut(sentence, cut_all=True)
print('全模式: ' + '/'.join(seg_list))

# 搜尋模式
seg_list = jieba.cut_for_search(sentence)
print('搜尋模式: ' + '/'.join(seg_list))

# 關鍵詞
seg_list = jieba.analyse.extract_tags(sentence, topK=5, withWeight=False)
print('關鍵詞: ' + '/'.join(seg_list))

# 加入停用詞
print('加入停用詞: ')
seg_list = jieba.cut(sentence)
filtered_words = [word for word in seg_list if word not in stopword]
print(" ".join(filtered_words))

# 計算詞彙出現次數
data={}
for word in filtered_words:
 if len(word)>=2:
  if word not in data:
    data[word]=0
  data[word]+=1
print(data)
print(type(data))
