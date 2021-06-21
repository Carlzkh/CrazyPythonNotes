import pymysql
# 链接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root2021', db='study', port=3306, charset='utf8')
# 获取游标
c = conn.cursor()
# 执行
c.execute('insert into user_tb values(null, %s, %s, %s)', ('孙悟空', '123456', 'male'))
c.execute('insert into order_tb values (null, %s, %s, %s, %s)', ('鼠标', '34.2', '3', 1))
conn.commit()
# 关闭游标
c.close()
# 关闭链接
conn.close()

