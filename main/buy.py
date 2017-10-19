# -*- coding:utf-8 -*-
import sys
sys.path.append('../')
from comments.read_file_name import file_name
from comments.read_xls import Read_xls_file

class buy_goods():

	def __init__(self):
		self.all_items,self.user_account,self.user_items,self.user_money = file_name()

	def get_all_items(self):
		'''获取所以商品'''
		return Read_xls_file(self.all_items).get_xls()

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
		name = raw_input('please input your name:')
		psw = raw_input('please input your password:')
		if int(self.get_user_account()[0][2]) == 0:
			print '你现在有金钱:%d'%(self.get_user_money())
			print '有如下商品:'
			print self.get_all_items()


	


	def main(self):
		print '你现在有金钱:%d'%(self.get_user_money())
		print '有如下商品:'
		print self.get_all_items()


buy_goods().main()


