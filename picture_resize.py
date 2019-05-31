#切割图片并保存exif信息
from PIL import Image
import os


for root,dirs,files in os.walk("D:\\python code\\data\\11-19"):
	for file in files:
		f=os.path.join(root,file)
		print(f)
		im  =Image.open(f)#打开图片
		#exif = im.info['exif']
		im2 =im.resize((1280,960))#改变图片大小
		#im2.save(f.replace('.jpg','resize.jpg'),exif=exif)
		im2.save(f.replace('.JPG','resize.jpg'))