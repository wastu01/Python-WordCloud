# https://colab.research.google.com/drive/1kaO0LbsOJVEBTee23UDjJxxP9emxBrB0


# https://tako-analytics.com/2023-06-19-how-to-extract-keywords-from-traditional-chinese-articles-in-nlp/
# only 斷詞

# from this tutorial
# https://blog.infuseai.io/nlp-tool-ckiptagger-introduction-e34637184e67

# 待研究


# # 引入 CkipTagger 套件中的斷詞(WS)、詞性標註(POS)、命名實體識別(NER)工具，
# # 以及資料下載與詞典建構函數
# from ckiptagger import data_utils, construct_dictionary, WS, POS, NER
#
# # 下載 CkipTagger 的預訓練模型，下載的路徑為"./"，並且生出data資料夾
# data_utils.download_data_gdown("./")
#
# # 初始化 WS(斷詞)、POS(詞性標註)、NER(命名實體識別) 的工具，模型路徑為 "./data"
# ws = WS("./data")
# pos = POS("./data")
# ner = NER("./data")
#
# # 建立一個詞典，詞典中的每個詞都有一個對應的權重
# word_to_weight = {
#     "土地公": 1,
#     "土地婆": 1,
#     "公有": 2,
#     "": 1,
#     "來亂的": "啦",
#     "緯來體育台": 1,
# }
#
# # 使用 construct_dictionary 函數來將上述的詞與權重建立成詞典
# dictionary = construct_dictionary(word_to_weight)
# print(dictionary)
#
# # 定義一個待進行處理的句子列表
# sentence_list = [ ... ]
#
# # 使用 WS 來對句子列表進行斷詞，並存入 word_sentence_list
# word_sentence_list = ws(sentence_list)
#
# # 使用 POS 來對斷詞後的句子列表進行詞性標註，並存入 pos_sentence_list
# pos_sentence_list = pos(word_sentence_list)
#
# # 使用 NER 來對斷詞、詞性標註後的句子進行命名實體識別，並存入 entity_sentence_list
# entity_sentence_list = ner(word_sentence_list, pos_sentence_list)
#
# # 釋放 WS、POS、NER 使用的記憶體
# del ws
# del pos
# del ner
#
# # 定義一個印出斷詞和詞性標註結果的函數
# def print_word_pos_sentence(word_sentence, pos_sentence):
#     assert len(word_sentence) == len(pos_sentence)
#     for word, pos in zip(word_sentence, pos_sentence):
#         print(f"{word}({pos})", end="\u3000")
#     print()
#     return
#
# # 迴圈印出每個句子的處理結果，包括斷詞、詞性標註以及命名實體識別的結果
# for i, sentence in enumerate(sentence_list):
#     print()
#     print(f"'{sentence}'")
#     print_word_pos_sentence(word_sentence_list[i],  pos_sentence_list[i])
#     for entity in sorted(entity_sentence_list[i]):
#         print(entity)