package utilTest;

public class GeneralMethod {
    public static void main(String[] args) {
        String st = "awwwabbcdd";
        //  System.out.println(convert(st));
        //System.out.println(convert1(st, 3));
        // stringTest01();
        test_for();
    }
    public static void test_for(){
        int i=-1;
        for(;++i<5;){

        }
        System.out.println(i); //这个i是验证不合格而退出的
    }
    public static void stringTest01(){
        String str="1222222222222";
        int num4=1234;
        int num=(int)Long.parseLong(str);
        //int num3=Integer.valueOf(str); //这两个方法的差异。数字过大会报错。
        long num2=Long.valueOf(str);  //长的怎么截断,long对象
        int num22=(int)num2;
        String str3=String.valueOf(num4); //不同对象调用valueof的
        int num1=000000320;
        System.out.println(str);
        System.out.println(num2);
    }
    public static void stringTest(){
        String str="abcde";
        String str1=str.substring(1); //begin and end
        //if(str.charAt[0]=="-"),这个语句有两个错误，说明对与java语言还是不够熟练
        // 没有提供反转的方法
        double num1=Math.pow(2.0,2.0); //全部是double类型的类型，java语言的特色

        System.out.println(str1);
    }
    public static String convert(String s) {
        StringBuffer sb = new StringBuffer();
        char c = s.charAt(0);
        int count = 1;
        sb.append(c);
        for (int i = 1; i < s.length(); i++) {
            if (c == s.charAt(i)) {
                count++;
            } else {
                sb.append(count);
                c = s.charAt(i);
                sb.append(c);
                count = 1;
            }
        }
        sb.append(count);
        return new String(sb);
    }
    public static void characterOperation(){  //做这个事情要一步一步来，不能太心急，一步一步操作。
        char ch='s';
        boolean boo=Character.isDigit(ch);
    }
    public static String convert1(String s, int numRows) {
            if (s.length() < 2) {
                return s;
            }
            char[] chars = s.toCharArray();
            int length = chars.length;
            char[] chars2 = new char[length];
            int point = 0;
            try {
            for (int i = 0; i < numRows; i++) {//寻找脚标数字规律的问题。
                boolean flag = true;
                int next1 = 0;
                int next2 = 0;
                int j = i;
                while (j < length) {//使用j访问数组，在访问时和length比较，保证不会越界。
                    if (i == 0 || i == numRows - 1) {
                        chars2[point] = chars[j];
                        point++;
                        j = 2 * (numRows - 1) + j;
                    } else {
                        if (flag) {
                            chars2[point] = chars[j];
                            flag = false;
                            next1 = j;
                            j = j + 2 * (numRows - i - 1); //下次的j;
                            next2 = j;
                        } else { //只可能存在point越界。
                            chars2[point] = chars[j];
                            point++;
                            if (next2 == j) {
                                next1 = next1 + 2 * (numRows - 1);
                                j = next1;
                            } else {
                                next2 = next2 + 2 * (numRows - 1);
                                j = next2;
                            }
                        }
                    }

                }
            }
        }catch (Exception e){
            e.printStackTrace();
        }
        return new String(chars2);
    }
}
