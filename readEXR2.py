import sys
import array
import OpenEXR
import Imath
import numpy
from PIL import Image
File = OpenEXR.InputFile("data/1_1_2_name.Depth.0000.exr") 
PixType = Imath.PixelType(Imath.PixelType.FLOAT) 
# DW = File.header()['dataWindow'] 
# Size = (DW.max.x - DW.min.x + 1, DW.max.y - DW.min.y + 1) 
Size = (1280,960)
rgb = [numpy.fromstring(File.channel(c, PixType), dtype=numpy.float32) for c in 'RGB'] 
r =numpy.reshape(rgb[0],(Size[1],Size[0])) 
g =numpy.reshape(rgb[1],(Size[1],Size[0])) 
b =numpy.reshape(rgb[2],(Size[1],Size[0]))

# for i in range(len(r)):
# 	print(i,r[i],g[i],b[i])
print(r[0][0])
newImg  =Image.open('timg.jpg').convert("L")
print(newImg.getpixel((611,612)))#查看像素，参数是元组形式
newImg.show()

A = []
print(r[606][635]*1146)
for i in range(0,960):#height
	for j in range(0,1280):#width
		k = int(r[i][j]*1146)
		A.append(k)
		#print(i,j,k)
		newImg.putpixel((j,i),int(r[i][j]*255))#修改像素，第一个参数是元组
newImg.show()
A.sort()
print(len(set(A)))