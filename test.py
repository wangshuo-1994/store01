import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='silentrebirth94', database='py1',
                       charset='utf8')
cursor = conn.cursor()
sql = 'insert into mytest(name) values(%s);'
try:
    for i in range(10000):
        cursor.execute(sql,['test'+str(i)])
    conn.commit()
except Exception as e:
    conn.rollback()
finally:
    cursor.close()
    conn.close()