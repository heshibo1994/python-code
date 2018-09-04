import sys
import array
import OpenEXR
import Imath
import numpy
File = OpenEXR.InputFile("1depth.exr") 
PixType = Imath.PixelType(Imath.PixelType.FLOAT) 
DW = File.header()['dataWindow'] 
Size = (DW.max.x - DW.min.x + 1, DW.max.y - DW.min.y + 1) 
rgb = [numpy.fromstring(File.channel(c, PixType), dtype=numpy.float32) for c in 'RGB'] 
r =numpy.reshape(rgb[0],(Size[1],Size[0])) 
g =numpy.reshape(rgb[1],(Size[1],Size[0])) 
b =numpy.reshape(rgb[2],(Size[1],Size[0]))

for i in range(len(r)):
	print(r[i],g[i],b[i])
