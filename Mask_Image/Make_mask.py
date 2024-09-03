from PIL import Image, ImageDraw

# 設定圖像大小
image_size = 512  # 圖像的寬度和高度
small_square_size = 20  # 每個小正方形的寬度和高度

# 讀取 color_list.txt 文件中的顏色
with open('/Users/larry/Github/Python-WordCloud/Mask_Image/color_list.txt', 'r') as f:
    # 讀取文件內容並將其轉換為列表
    colors = f.readline().strip().split(",")
    print(type(colors))

# 創建空白圖像
img = Image.new("RGB", (image_size, image_size), "white")
draw = ImageDraw.Draw(img)

# 畫小正方形並填充顏色
color_index = 0
for i in range(0, image_size, small_square_size):
    for j in range(0, image_size, small_square_size):
        # 選擇顏色
        color = colors[color_index % len(colors)]
        # 畫小正方形並填充選定的顏色
        draw.rectangle([i, j, i + small_square_size, j + small_square_size], fill=color)
        # 更新顏色索引
        color_index += 1

# # 儲存圖片
img.show()
img.save("Square_mask.png")
