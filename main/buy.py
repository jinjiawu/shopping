# -*- coding:utf-8 -*-
import sys
sys.path.append('../')
from comments.read_file_name import file_name
from comments.read_xls import Read_xls_file

class buy_goods():

	def __init__(self):
		self.all_items,self.user_items,self.user_money = file_name()

	def login(self):
		name = raw_input('please input your name:')
		psw = raw_input('please input your password:')

	def get_all_items(self):
		return Read_xls_file(self.all_items).get_xls()

	def main(self):
		print self.get_all_items()

buy_goods().main()


