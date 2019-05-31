import cv2 
img_root = "D://python code//data//mynteye_test_1//"#这里写你的文件夹路径，比如：/home/youname/data/img/,注意最后一个文件夹要有斜杠 
fps = 15 #保存视频的FPS，可以适当调整 
size=(1280,720) #可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg 
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
videoWriter = cv2.VideoWriter("D://python code//data//myntete_test_1.avi",fourcc,fps,size)
#最后一个是保存图片的尺寸 #
for i in range(118): 
	print(i)
	frame = cv2.imread(img_root+"frame"+"0"*(4-len(str(i)))+str(i)+'.jpg') 
	videoWriter.write(frame) 
videoWriter.release()