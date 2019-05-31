# 提取视频中的每一帧图片
import cv2

vc = cv2.VideoCapture('data//20190514factory//DJI_0032.MOV')  # 读入视频文件
c = 1
rval, frame = vc.read()

while rval:
	# 循环读取视频帧
	rval,frame = vc.read()
	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Display the resulting frame
	#cv2.imshow('frame', frame)

	if c % 60 == 0:
		cv2.imwrite('data//20190514factory//data2//' + str(c) + '.jpg', frame)  # 存储为图像
		print(c)
	c = c + 1
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
   
vc.release() 
cv2.destroyAllWindows()