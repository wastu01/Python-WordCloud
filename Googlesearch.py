import os
import re
import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup

now = datetime.now()
# print(now)

query = '新竹'

time_str = now.strftime("%m%d%H%M")

folder_name = now.strftime("%Y-%m-%d")+ "-" + query
os.makedirs(folder_name, exist_ok=True)

# 注意，headers 要用字典格式，並加上引號
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15'}

url = 'https://www.google.com/search?q=' + query
print(url)
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
print(f'soup 資料型態: {type(soup)}')
# print(soup)

# content = soup.find_all(class_="LC20lb")
# <h3 class="LC20lb MBeuO DKV0Md">新竹縣旅遊網-首頁</h3>
# <h3 class="LC20lb MBeuO DKV0Md">新竹熱門旅遊景點</h3>

# print(content)
# for elem in content:
#     print(elem.prettify())

# 更好的方式
# 儲存標題
titles = []
descriptions = []

content = soup.find_all('div', class_='g')
for elem in content:
    title = elem.find('h3')
    if title:
        titles.append(title.get_text())
    
    span = elem.find_all('span')
    if len(span) > 1:
        descriptions.append("".join([s.get_text() for s in span]))
    
    # print(descriptions)

# print(titles)
# print(descriptions)

data = {}  # 初始化字典來存儲 title 和 description

# 使用 zip 將 titles 和 descriptions 一起遍歷，並存入 data
for title, desc in zip(titles, descriptions):
    data[title] = desc

print(data)

# 設定 JSON 檔案路徑
json_file_path = os.path.join(folder_name, f'search_results_{time_str}.json')


# 將資料寫入 JSON 檔案
with open(json_file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


# print('Google搜尋結果的標題:')
# print(titles)
# print(f'titles 資料型態: {type(titles)}')



