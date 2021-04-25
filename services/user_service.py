#对学生进行增删改查  业务逻辑层 调用base_mysql
#import pymysql
#把mysql 文件导入进来
from mysql.base_mysql import Mysql

class UserService():

    def __init__(self):
        #创建一个对象
        self.m = Mysql()

    # 添加学生
    #1 def add_atu(self,name, age, sex, classes,card, city)
    def add_stu(self,*args):
        # 1.确定用户数据，组装成SQL语句
        lst = list(args)
        while len(lst) <= 6:
             lst.append('')

        #1  sql = "insert into students(name,age,sex,class,card,city) values('{}',{},‘{}’，'{}','{}','{}')".format(name,age,sex,classes,card,city)
        sql = "insert into students(name,age,sex,class,card,city) values('{}',{},‘{}’，'{}','{}','{}')".format(*lst)

    #2.用update实现插入学生的操作
        # if not isinstance(age,int):
        #     return '输入数据类型错误,年龄要求输入整数‘
        # if age < 0:
        #     return '年龄输入不正确'
        result = self.m.update(sql)
    #3.给出用户提示
        #如果不为空
        if not result:
           print('添加学生纪录成功')
        else:
           print('添加学生记录失败')
    #删除学生
    def del_stu(self,age):
        sql = "delect from students where age = {}".format(age)
        # sql = "delect  from  students where name like '%{}%'".format(name)
        result = self.m.get_all(sql)
        return result
        # 如果不为空
        if not result:
            print('删除学生纪录成功')
        else:
            print('删除学生记录失败')
    #修改学生信息
    def mod_stu(self,column,value,name):
        if str(value).isdigit():  #判断是否为整数
           sql = "update students set {} = {} where name like '%{}%'".format(column,value,name)
        else:#认为他是字符串
            sql = "update students set {} = '{}' where name like '%{}%'".format(column, value, name)
        #用self调用update
        result = self.m.update(sql)
        # 如果不为空
        if not result:
            print('修改学生纪录成功')
        else:
            print('修改学生记录失败')

    #查询学生
    def get_stu(self,name):
    #def get_stu(self, age):
         #sql = "select *from students where age = {}".format(age)
         sql = "select * from  students where name like '%{}%'".format(name)
         result = self.m.get_all(sql)
         return result
#main 函数为入口脚本
if __name__ == '__main__':
    us = UserService()
    #sql = "name='主管'，age=24,sex='男',class='7班',card='100200300400',city='上海'"
    us.add_stu('主管',40,'男','7班','1000100030004000','上海')
    #us.mod_stu('class','7班','王剪')
    #print(us.get_stu('王'))
    #print(us.get_stu(29))
    #print(us.del_stu())