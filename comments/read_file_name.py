# -*- coding:utf-8 -*-
import os

def file_name():
	for root,dirs,files in os.walk(os.path.dirname(os.path.abspath('.'))+'\\testData\\'):
		return files #当前路径下所有非目录子文件
print file_name()