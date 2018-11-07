package utilTest;

import java.util.regex.Pattern;

public class RegularExpression {
    public static  void test01(){
        String regex="^d{4}";
        Pattern pattern = Pattern.compile("^[-\\+]?[\\d]*$"); //匹配整数，\\在java要转义
    }
    public static  void test02(){
        //最简单的使用string的match和replace函数。Pattern和Match类
        //匹配邮箱
        String regex="^.+@.+(\\..+){1,}$";
        String str="fushb@163.com";
        System.out.println(str.matches(regex));

        //匹配固定电话  4位区号-7位号码 或者 3位区号-8位号码
        String regex2="^\\d{4}-\\d{7}|\\d{3}-\\d{8}$";  //右斜线在java的字符串中有特殊的意义。
        String str2="020-13222113";
        String str3="0532-9989211";
        System.out.println(str2.matches(regex2));
        System.out.println(str3.matches(regex2));

        //匹配除了a和9之外的数字或字符
        String regex3="^[^9a]{1,}$";//^在括号里面和括号里面的差别。
        String str4="1234fsfse";
        String str5="a2343";
        System.out.println(str4.matches(regex3));
        System.out.println(str5.matches(regex3));

        //^和$的用法
        String a = "3131sasfasd".replaceAll("\\d{2}", "Z");
        String b = "3131sasfasd".replaceAll("^\\d{2}", "Z");//仅替换字符串开头的两个数字
        String c = "3131sdasfasd".replaceAll("sd", "Z");
        String d = "3131sdsfasd".replaceAll("sd$", "Z");//仅替换字符串开头的两个数字
        System.out.println(a);//ZZZsasfasd
        System.out.println(b);//Z3131sasfasd
        System.out.println(c);//aa3131ZasfaZ
        System.out.println(d);//aa3131sdsfaZ
        String str6 = "aa3131sasfasd";
        System.out.println(str6.matches("\\d{2}")); //false
        System.out.println(str6.matches("^\\d{2}"));//false
    }

    public static void main(String[] args) {
        test01();
        test02();
    }
}
