import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root2021', db='study', port=3306)
c = conn.cursor()
c.execute('select * from user_tb where user_id>%s', (2,))
for col in c.description:
    print(col[0], end='\t')
print('\n--------------------------------')

for row in c:
    print(row)
    print(row[1] + '-->' + row[2])

c.close()
conn.close()

