package utilTest;

public class ObjectRef {

    public static void main(String[] args) {
        Num num=new Num();
        Num num_ref=num; //  改变num的引用，测试num会不会变。
        Num1 num1=new Num1(7,8);
        num_ref.a=6;
        num_ref.num1=num1; // num1的命名空间
        System.out.println(num.a);
        System.out.println(num_ref.a);
        System.out.println(num.num1.a);
        System.out.println(num_ref.num1.a);
        test_var(num);  //对象的属性值被改变了,并没有把对象的值copy一份给函数。
        System.out.println("****************");
        System.out.println(num.a);
        System.out.println(num_ref.a);
        System.out.println(num.num1.a);
        System.out.println(num_ref.num1.a);
    }
    public static void test_var(Num num){
        num.a=19%10; // 取余数的运算
        double b=19.0/10;
        // float c=1233.23;默认是double类型
        
        num.num1.a=19/10;
        System.out.println(num.a);
        System.out.println(num.num1.a);
    }
}
class Num{
    int a=4;
    int b=3;
    Num1 num1=new Num1(4,3);
}
class Num1{
    int a;
    int b;
    Num1(int a, int b){
        this.a=a;
        this.b=b;
    }
}
