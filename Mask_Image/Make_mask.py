from PIL import Image, ImageDraw
import random

# 設定圖像大小
image_size = 512  # 圖像的寬度和高度
small_square_size = 20  # 每個小正方形的寬度和高度
num_colors = image_size**2 // small_square_size**2
print(num_colors)

# 讀取 color_list.txt 文件中的顏色
with open('/Users/larry/Github/Python-WordCloud/Mask_Image/color_list.txt', 'r') as f:
    # 讀取文件內容並將其轉換為列表
    colors = f.readline().strip().split(",")
    print(len(colors))

# 創建空白圖像
img = Image.new("RGB", (image_size, image_size), "white")
print(type(img))
# Pillow Image 影像物件

draw = ImageDraw.Draw(img)
print(type(draw))
# Pillow ImageDraw 繪圖物件

# 畫小正方形並填充顏色
n = 80
for i in range(0, image_size, small_square_size):
    for j in range(0, image_size, small_square_size):
        # 選擇顏色
        # color = random.choice(colors)
        color = colors[num_colors % len(colors)]
        # 畫小正方形並填充選定的顏色
        draw.rectangle([i, j, i + small_square_size, j + small_square_size], fill=color)
        # 更新顏色索引
        num_colors += n
        # print(color)

# Pillow 畫圖是以左上角為原點 (0,0)
# 參數是 左上角座標, 右下角座標
# https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html


img.show()
img.save(f"./Mask_Image/Square_mask_pattern_{n}.png")
