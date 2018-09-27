import pymysql

class DB :
    my_config = {
        'host': '127.0.0.1',  #  localhost,不是host
        'user': 'root',
        'password': 'baibai123',
        'port': 3306,
        'database': 'liyong_test'
    }

    @staticmethod
    def get_con():
        con = pymysql.connect(**DB.my_config)
        return con

"""sql = \"""
      CREATE TABLE XIAOHUAR(
      ID INT PRIMARY KEY AUTO_INCREMENT,
      NAME VARCHAR(50),
      AGE VARCHAR(50),
      SCHOOL VARCHAR(50),
      JOB VARCHAR(50),
      MAJOR VARCHAR(50),
      CONSTELLATION VARCHAR(50)
      )
\"""

cursor = DB.get_con().cursor()
cursor.execute(sql)
"""