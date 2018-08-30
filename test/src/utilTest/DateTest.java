package utilTest;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class DateTest {
    static Date date01 = new Date();
    static Calendar calendar = Calendar.getInstance();  //no parameter,how to the pattern;
    static Calendar calendar01 = Calendar.getInstance();
    static Date date = new Date(); //

    static SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss"); //
    static SimpleDateFormat sdf01 = new SimpleDateFormat("yyyy-MMMM-dd EEEE HH:mm:ss");// 大写表示24小时制,EEEE代表汉语星期

    public static void proProcess() {
        calendar.setTime(date01); //Date对象和Calendar对象的相互转换
        calendar01.add(Calendar.DATE, 100); //得到100天后的日期，日期的计算，calendar很方便
    }

    public static void main(String[] args) {
        proProcess();
        System.out.println(calendar);
        System.out.println(date);
        System.out.println(calendar.get(Calendar.DAY_OF_WEEK));
        System.out.println(sdf.format(calendar01.getTime()));
        System.out.println(sdf01.format(calendar.getTime()));

    }
}
