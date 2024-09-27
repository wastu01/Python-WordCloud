from bs4 import BeautifulSoup

# 讀取 HTML 文件
with open('/Users/larry/Github/Python-WordCloud/check-datatype/Googlesearch_org.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# 移除 <head> 和 <meta> 區域
if soup.head:
    soup.head.decompose()

# 移除所有 <script> 標籤
for script in soup.find_all('script'):
    script.decompose()
   
# https://blog.csdn.net/yezi1993/article/details/111280992

# 只保留 <body> 區域並格式化顯示
body_content = soup.body
# 使用 prettify 格式化輸出
if body_content:
    print(body_content.prettify())
else:
    print("No body content found.")
    
# 將處理後的內容存為新檔案
with open('filtered_body_content.html', 'w', encoding='utf-8') as new_file:
    new_file.write(body_content.prettify() if body_content else "No body content found.")
