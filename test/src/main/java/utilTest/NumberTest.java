package utilTest;

import java.math.BigInteger;

public class NumberTest {
    public static void main(String[] args) {
        //test("9646324351");
        stringBound(null);
        stringBound("  ");
        stringBound("   sdfds");
        String st="  ";
        String str=new String("asdf");
        String str2=new String("asdf");
        System.out.println(str==str2);
        System.out.println(str.equals(str2));
        System.out.println(st+"dsd");
        System.out.println(st.trim()+"dsd");
    }
    public static void stringBound(String str){

        if(str==null||!str.trim().equals("")){  //trim是在元来基础上修改，但是不是用str。trim()=="";
            //对象和基本类型在比较操作时的差异
            System.out.println("this is not a normal string");
            return;
        }
        str.trim();
        System.out.println("this is a normal string");

    }
    public static void test(String x){//"9646324351"，转换过来可能就出了int的范围
        //2e31 - 1 = 2147483647 //20亿，signed int的范围就这么大123457678900088784398429834718
        double num=Double.parseDouble(x);
        String str="  fds  ";
        String str1=str.trim();//去掉前后空格的函数，当然也可以自己写，但是jdk提供了，很方便。
        if(num>Math.pow(2.0,31)){
            System.out.println("the number is too large");
        }
        System.out.println(Integer.MAX_VALUE); //这是一个常数。
    }
    public static int reverse(int  x) {
        if(x>=(double)Math.pow(2.0,31.0)||x<(double)-Math.pow(2.0,31.0)){
            return 0;
        }
        String str=String.valueOf(x);
        boolean negative=false;
        if(str.charAt(0)=='-'){
            negative=true;
        }
        if(negative){
            str=str.substring(1);
        }
        char ch;
        char[] chars=str.toCharArray();
        for(int i=0;i<chars.length/2;i++){ //对这个字符串进行反转
            //这种操作还是转换为数组方便
            ch=chars[i];
            chars[i]=chars[chars.length-i-1];
            chars[chars.length-i-1]=ch;
        }
        String str1=new String(chars);
        System.out.println(str1);
        int num=Integer.parseInt(str1);
        if(negative){
            num=-num;
        }
        return num;
    }
}
