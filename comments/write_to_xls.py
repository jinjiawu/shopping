# -*- coding:utf-8 -*-
import sys
sys.path.append('../')
from log import Logger
from read_xls import Read_xls_file
import os.path
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy

logger = Logger('write_xls').getlog()

def write_to_excel(value,file_name):
	#根据要写入的值value写入到表file_name中
	file_path = os.path.dirname(os.path.abspath('.'))+'\\testData\%s'%file_name
	rb = open_workbook(file_path)
	wb = copy(rb)
	#通过get_sheet()获取的sheet有write()方法,这里是获取第一个页签的内容
	ws = wb.get_sheet(0)
	if file_name == 'user_money.xlsx':
		#在第2行第1列写入数据
		ws.write(1,0,value)
		
	#将购买到的商品写入到该表中
	if file_name == 'user_items.xlsx':
		#先获取现有的物品行数
		rows = len(Read_xls_file('user_items.xlsx').get_xls())
		#在最新行的第1列写入数据
		ws.write(rows+1,0,value)
	#将登录次数写入到该表中
	if file_name == 'user_account.xlsx':
		ws.write(1,2,value)
	#保存excel
	wb.save(file_path)

