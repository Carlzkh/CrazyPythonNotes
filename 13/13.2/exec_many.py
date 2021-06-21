import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root2021', db='study', port=3306)
c = conn.cursor()
c.executemany('insert into user_tb values(null, %s, %s, %s)',
              (('sun', '123456', 'male'),
               ('bai', '123456', 'female'),
               ('zhu', '123456', 'male'),
               ('niu', '123456', 'male'),
               ('tang', '123456', 'male')))
conn.commit()
c.close()
conn.close()
