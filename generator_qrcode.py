# import qrcode 
# qr = qrcode.QRCode(     
#     version=1,     
#     error_correction=qrcode.constants.ERROR_CORRECT_L,     
#     box_size=10,     
#     border=4, 
# ) 
# qr.add_data('hello, qrcode') 
# qr.make(fit=True)  
# img = qr.make_image()
# img.save('123.png')


# version：值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）。 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。

# error_correction：控制二维码的错误纠正功能。可取值下列4个常量。
# 　　ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
# 　　ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
# 　　ROR_CORRECT_H：大约30%或更少的错误能被纠正。

# box_size：控制二维码中每个小格子包含的像素数。

# border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）

import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
# print(random.choice([1,3,5]))
# from PIL import Image
# im1  =Image.open('D:\\python code\\data\\qr_code\\0.jpg')
# im2 = im1.resize((7,7))
# for i in range(0,7):
# 	for j in range(0,7):
# 		im2.putpixel((i,j),(0,0,0))#修改像素，第一个参数是元组
# im2 = im2.resize((980,980))
# im2.save('D:\\python code\\data\\qr_code\\temp.jpg')
# im2.show()

l = 630
im1  =Image.open('D:\\python code\\data\\qr_code\\temp.jpg')
im1  = im1.resize((7,7))
for n in range(20):
	for i in range(1,6):
		for j in range(1,6):
			k =random.choice([0,255])
			print(k)
			im1.putpixel((i,j),(k,k,k))
	im2 = im1.resize((l,l))
	im2.save('D:\\python code\\data\\qr_code\\'+str(n)+'.jpg')
	width = l
	height = l
	image = Image.new('RGB', (width, height), (255, 255, 255))
	font=ImageFont.truetype('simsun.ttc',180)
	# 创建Draw对象:
	draw = ImageDraw.Draw(image)
	text = str(n)
	draw.text((10,10), text, font=font, fill="#000000", spacing=0, align='left') 
	image.save('D:\\python code\\data\\qr_code\\'+str(n)+'_rt.jpg')
