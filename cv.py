import cv2 # 导入库
file = "data/1_1_2_name.Depth.0000.exr" # 定义图片地址
img = cv2.imread(file) # 读取图像
print(img.width)
cv2.imshow('image', img) # 展示图像
cv2.waitKey(0) # 与显示参数配合使用