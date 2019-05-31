import sys
import array
import OpenEXR
import Imath
import cv2
from PIL import Image

newImg = Image.new("RGBA",(1280,960),(0,255,0))
newImg.save("newImg.png","PNG")
#newImg.show()


# Open the input file
file = OpenEXR.InputFile("data/1_1_2_name.Depth.0000.exr")
(r, g, b) = file.channels("RGB")
# for i in range(len(r)):
# 	print(i,r[i],g[i],b[i])
for i in range(0,1280):
	for j in range(0,960):
		newImg.putpixel((i,j),(r[i*1280+j],g[i*1280+j],b[i*1280+j]))#修改像素，第一个参数是元组
newImg.show()
for i in range(len(r)):
	print(r[i])
# Compute the size
#dw = file.header()['dataWindow']
#sz = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)
sz=(1280,960)
# Read the three color channels as 32-bit floats
FLOAT = Imath.PixelType(Imath.PixelType.FLOAT)
(R,G,B) = [array.array('f', file.channel(Chan, FLOAT)).tolist() for Chan in ("R", "G", "B") ]

# # Normalize so that brightest sample is 1
# #brightest = max(R + G + B)
# #R = [ i / brightest for i in R ]
# #G = [ i / brightest for i in G ]
# #B = [ i / brightest for i in B ]
# for i in range(len(R)):
#     print(i,R[i])
# # Convert to strings
# (Rs, Gs, Bs) = [ array.array('f', Chan).tostring() for Chan in (R, G, B) ]

# Write the three color channels to the output file
#out = OpenEXR.OutputFile("1.hdr", OpenEXR.Header(sz[0], sz[1]))
#out.writePixels({'R' : Rs, 'G' : Gs, 'B' : Gs })
