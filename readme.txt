一.作业需求：

1、启动程序后，输入用户名密码后，如果是第一次登录，让用户输入工资，然后打印商品列表

2、允许用户根据商品编号购买商品

3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒

4、可随时退出，退出时，打印已购买商品和余额

5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示

6、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买

7、允许查询之前的消费记录

 

二.购物车用户信息：

{'name': {'password': '10000'}, 'cx': {'123': '725.0'}, 'even': {'qw': '1560'}, 'cv1': {'1': 100.5}}
以字典形式存储用户名，密码，余额

三.历史购物信息：

{'name': [['iphone', 5800], ['bike', 800]], 'cx': [['iphone', 5800], ['apple', 5],  ['apple', 5], ['book', 75]]}
以字典形式，对应用户名和历史购物记录