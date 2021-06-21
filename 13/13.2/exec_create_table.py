import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root2021', db='study', port=3306)
c = conn.cursor()
# c.execute('''create table user_tb(user_id int primary key auto_increment,
#                                   name varchar(255),
#                                   pass varchar(255),
#                                   gender varchar(255))''')
c.execute('''create table order_tb(order_id integer primary key auto_increment,
item_name varchar(255),
item_price double,
item_number double,
user_id int,
foreign key(user_id) references user_tb(user_id))''')
c.close()
conn.close()
