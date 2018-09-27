import pymysql


##  con = mysql.connector, 只使 import MySQL 会报错

"""
 默认utf8（该格式书写）
 http://www.taobao.com
 mysql的访问路径：jdbc:mysql://localhost:3306/name
 ip地址前面都是类似于协议一样的东西
"""


def get_con():
    config = {
        'host': 'localhost',
        'user': 'root',
        'port': 3306,
        'password': 'baibai123',
        'database': 'liyong_test'

    }
    con = pymysql.connect(**config)  # 传入一个字典参数
    return con


con = get_con()
cursor = con.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

""" 
字符串的这种写法可以按照原样输出
"""
sql_create = """CREATE TABLE EMPLOYEE(
                 FIRST_NAME CHAR(20) NOT NULL PRIMARY KEY ,
                 LAST_NAME CHAR(20),
                 AGE INT,
                 SEX CHAR(1),
                 INCOME FLOAT)
"""
def test():
    cursor.execute(sql_create)
    sql_query = "select name,school from student_less;"
    sql_insert_data = "insert into student_less(name,age,school) values (%s,%d,%s)" % (
        '黎勇', 23, '四川师范大学')
    sql_insert = "insert into student_less(name,age,school) values (%s,%s,%s)"
    cursor.execute(sql_query)
    print(cursor.fetchone())   # 取出一条记录（记录用tuple的结构返回）
    print(cursor.fetchall())   # 取出全部数据
    for name, school in cursor:
        print(name, school)
    cursor.execute(sql_insert, ('李勇', 21, '四川交通大学'))
    con.commit()  # 还要提交至数据库执行
    cursor.close()
    con.close()


test()