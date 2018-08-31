package utilTest;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

/**
 * 不使用框架，java操作数据库，适合处理数据使用。
 * create table student_less
 * (
 * id int primary key auto_increment,
 * name varchar(255),
 * age int,
 * school varchar(110)
 * );建表语句varchar要指定长度，否则报错。
 * jdbc的驱动
 */
public class DatabaseUseJdbc {
    public static void main(String[] args) {
        String sqlInsert = "insert into student_less(name,age,school) values(?,?,?)"; //？占位符,和特定类相关。
        Student st = new Student("黎勇", 23, "四川大学");
        try {
            PreparedStatement ps = ConnectToDB.getConnection().prepareStatement(sqlInsert);
            ps.setString(1, st.name);
            ps.setInt(2, st.age);
            ps.setString(3, st.school);
            ps.execute();
            String sqlSelect="SELECT name,age,school FROM  student_less";
            ps=ConnectToDB.getConnection().prepareStatement(sqlSelect);
            ResultSet rs=ps.executeQuery();
            List<Student> ls=new ArrayList<>();
            while (rs.next()){  //逐个字段取出
                Student st1=new Student(); //还要定义空空构造函数
                st1.setName(rs.getString(1)); //ResultSet的索引从1开始,手动完成实体类到数据库记录的映射。
                st1.setAge(rs.getInt(2));
                st1.setSchool(rs.getString(3));
                ls.add(st1);
            }
            System.out.println(ls.size());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}

/**
 * 连接数据库需要给出哪些变量
 */
class ConnectToDB {
    //典型的url地址：jdbc:mysql://localhost:3306/liyong_test
    static String userName = "root";
    static String dbName = "liyong_test";
    static String pwd = "baibai123";
    static String ip = "localhost";
    static String port = "3306";
    static String driver = "com.mysql.cj.jdbc.Driver"; //5.X版本为com.mysql.jdbc.Driver
    static String append="?useUnicode=true&character=UTF-8&useSSL=false&serverTimezone=Asia/Shanghai";
    static String url = "jdbc:mysql://" + ip + ":" + port + "/" + dbName+append; //服务器地址

    public static Connection getConnection() {
        Connection con = null;
        try {
            Class.forName(driver);
            con = DriverManager.getConnection(url, userName, pwd);// 连接上，为关键的一步。
        } catch (Exception e) {
            e.printStackTrace();
        }
        return con;
    }

}
