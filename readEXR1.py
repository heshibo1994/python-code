import sys
import array
import OpenEXR
import Imath

# Open the input file
file = OpenEXR.InputFile("1depth.exr")

# Compute the size
dw = file.header()['dataWindow']
sz = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)

# Read the three color channels as 32-bit floats
FLOAT = Imath.PixelType(Imath.PixelType.FLOAT)
(R,G,B) = [array.array('f', file.channel(Chan, FLOAT)).tolist() for Chan in ("R", "G", "B") ]

# Normalize so that brightest sample is 1
#brightest = max(R + G + B)
#R = [ i / brightest for i in R ]
#G = [ i / brightest for i in G ]
#B = [ i / brightest for i in B ]
for i in R:
    print(i)
# Convert to strings
(Rs, Gs, Bs) = [ array.array('f', Chan).tostring() for Chan in (R, G, B) ]

# Write the three color channels to the output file
#out = OpenEXR.OutputFile("1.hdr", OpenEXR.Header(sz[0], sz[1]))
#out.writePixels({'R' : Rs, 'G' : Gs, 'B' : Gs })