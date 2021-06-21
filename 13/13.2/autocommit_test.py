import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root2021', db='study', port=3306)
conn.autocommit(True)  # conn.autocommit = True 设置无效
c = conn.cursor()

c.executemany('insert into order_tb values(null, %s, %s, %s, %s)',
              (('键盘2', '52.5', '2', 2),
               ('书包2', '36', '1', 3),
               ('显卡2', '3200', '1', 4),
               ('CPU2', '7800', '1', 5),
               ('内存2', '320', '2', 6)))
# conn.commit()  # 有conn.autocommit(True)，就无需这一行了
c.close()
conn.close()
