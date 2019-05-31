import os, sys
import shutil 
"""
将filePath文件下的图片保存在newFilePath文件夹下的相应子文件夹中
pic 是字典，存放每个图片要移到的子文件夹名
"""
def movefile(filePath, newFilePath):

	for root, dirs, files in os.walk(filePath):
		for f in files:
			fl = filePath + '\\' + f
			print(fl)
			no = int(f[5:9])
			if 1130<=no and no<=3430 and no%20 ==0:
				newFilePath = fl.replace("mynteye_pict","mynteye_pict_1")
				shutil.copyfile(fl,newFilePath) # 复制文件，都只能是文件

if __name__ == '__main__':
	movefile("D:\\python code\\data\\mynteye_pict","D:\python code\data\mynteye_pict_1")
 