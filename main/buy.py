# -*- coding:utf-8 -*-
import sys
sys.path.append('../')
from comments.read_file_name import file_name
from comments.read_xls import Read_xls_file
from comments.write_to_xls import *

class buy_goods():
	#先将登录设为false
	is_login = False

	def __init__(self):
		self.all_items,self.user_account,self.user_items,self.user_money = file_name()

	def get_all_items(self):
		'''获取所有商品'''
		item_list = Read_xls_file(self.all_items).get_xls()
		print item_list
		for i in xrange(len(item_list)):
			pass

	def get_user_account(self):
		'''获取用户帐号信息'''
		return Read_xls_file(self.user_account).get_xls()

	def get_user_items(self):
		'''获取用户已购买的物品'''
		return Read_xls_file(self.user_items).get_xls()

	def get_user_money(self):
		'''获取用户金钱'''
		return int(Read_xls_file(self.user_money).get_xls()[0][0])

	def login(self):
		'''用户登录'''
		while True:
			name = raw_input('please input your name:')
			psw = raw_input('please input your password:')
			#先判断登录帐号和密码是否正确
			if name == self.get_user_account()[0][0] and psw == str(self.get_user_account()[0][1]):
				#通过登录次数判断是不是第一次登录
				if int(self.get_user_account()[0][2]) == 0:
					salary = raw_input('please input your salary:')
					#将钱写入到表中
					write_to_excel(salary,'user_money.xlsx')
					#将登录次数写入到表中
					'''这里要添加登录次数的函数'''
					#打印金钱跟商品
				print '你现在有金钱:%d'%(self.get_user_money())
				print '有如下商品:'
				print self.get_all_items()
				#登录成功后登录状态为true
				is_login = True
				break
			else:
				print(u'用户名或者密码出错，请重新登录！')

	def buy_goods(self):
		'''购买商品'''
		last_money = int(self.get_user_money())
		while True:
			print(u'如果想要退出，就输入q')
			print(u'输入物品编号来购买物品')
			your_input = raw_input('please input your num:')
			if your_input == 'q':
				#将剩余的钱写入到表格中
				write_to_excel(last_money,'user_money.xlsx')
				break



	


	def main(self):
		print '你现在有金钱:%d'%(self.get_user_money())
		print '有如下商品:'
		self.get_all_items()


buy_goods().main()


