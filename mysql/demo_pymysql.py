#buzou

#1  导包
import pymysql

#2 创建数据库对象：connect()
conn = pymysql.connect(host=';localhost',user='root',password='root',database='school',charset='utf-8')

#3创建游标对象
cursor = conn.cursor()

#4对数据进行增删改查，都是使用的游标对象
sql = ''
cursor.execute(sql)


#5关闭游标对象
cursor.close()


#6关闭数据库连接
conn.close()