import java.util.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class LeetcodeProblem {
    public static void main(String[] args) {
        arrayOutOfIndex();
    }
    public static void less(){
        int con=0;
        int a,b,c;
        int a1=1,b1=4; //more elegant
        while (con<10){
            char ch='y';
            String st="ds";
            switch (con){
                case 2:
                    System.out.println("the value is 2");
                    ch='f';
                    break;
                case 34:
                    System.out.println("the value is 3");
                    break;
                default:
                    System.out.println("is uncertain");
            }
            con++;
            switch (ch){

            }
            switch (st){  //字符串和字符都是可以的，但是类型要统一。

            }
        }
    }
    public boolean isMatch(String text, String pattern) {
        //把这个代码转化为流程图是怎样的？

        //考虑这些情况，看看有没有思路。aaa, a.*b;aaab,aa*b;
        if (pattern.isEmpty()) return text.isEmpty(); //归结为了很简洁的语句
        boolean first_match = (!text.isEmpty() && //先判断了text是否为空，
                (pattern.charAt(0) == text.charAt(0) || pattern.charAt(0) == '.'));

        if (pattern.length() >= 2 && pattern.charAt(1) == '*'){
            return (isMatch(text, pattern.substring(2)) ||
                    (first_match && isMatch(text.substring(1), pattern)));  //不段的向后移动
        } else {
            return first_match && isMatch(text.substring(1), pattern.substring(1));
        }
    }
    public static void arrayOutOfIndex(){
        String[] st={};  //空数组是一种什么情况?
        String[] st1={"sf"};
        String[] st2={"sf","gh"};
        System.out.println(st.length);
        System.out.println(st1.length);
        System.out.println(st2);
        //数组的null和[]是两个不同的东西
    }
    public int romanToInt(String s) {
        Map<Character, Integer> map = new HashMap<>(); //因为字母不能为下脚标，所以使用Map数据结构
        // List<Integer> ls=new ArrayList<>(12,32,23);
        //List<List<Integer>> ls=new ArrayList<ArrayList<Integer>>();
        List<ArrayList<Integer>> ls=new ArrayList<ArrayList<Integer>>();
        List<Integer> ls1=new ArrayList<>();
        ls1.add(23);
       //  ls.add(ls1); 这个有语法错误
        map.put('I', 1); //降低错误率
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        //  int num1=map.getValue(s.charAt(0));
        /* int num=num1;
        for(int i=1;i<s.length;i++){
            int num2=map.getValue(s.charAt(i)); 一段错误的代码，看自己做的怎么样。
            if(num2>num1){
                num-=2*num1;
            }
            num+=num2;
            num1=num2;
        }
        return num;
    }*/
        return 4;
       }

}
