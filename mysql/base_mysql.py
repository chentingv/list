#1  导包  数据访问层
import pymysql
#调用配置文件
from settting import DB_CONFIG
class Mysql(object):


    def __init__(self):
        self.conn = pymysql.connect(**DB_CONFIG)
#实现查询方法
    def get_all(self,sql):
        try:
            #cursor = self.conn.cursor()
            #创建游标对象
            with self.conn.cursor() as cursor:
                #执行SQL语句
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)
        finally:
            if self.conn:
                #关闭游标对象
                self.conn.close()

    #实现修改方法
    def update(self,sql):
        try:
            # 创建游标对象
            #with 当代码执行完成后关闭游标对象
            with self.conn.cursor() as cursor:
                # 执行SQL语句  SQL为变量
                cursor.execute(sql)
                #提交
                self.conn.commit()
        except Exception as e:
            #回宫操作 回到原始状态
            self.conn.rollback()
            print(e)
        finally:
            if self.conn:
                self.conn.close()
if __name__ == '__main__':
    sql = "select * from students where age= 30"
    sql1 = "update students set age = 40 where studentNo = 5 "
    m= Mysql()
    #print(m.get_all(sql))
    m.update(sql1)