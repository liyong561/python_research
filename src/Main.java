import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.*;
import java.util.concurrent.ExecutionException;

public class Main {
    /**
     * this can introduce the method
     * @param n
     * @param obj
     */
    public static  void print(int n,Object obj){
      //  System.out.println("{%d,%s}",n,obj.toString()); this is wrong
        System.out.println(String.format("{%d,%s}",n,obj.toString()));
    }
    public  static  void demoString(){ // no need prama
        String str="Hello,liyong";
        print(2,str.indexOf("2"));
        print(3,str.indexOf("el")); //index start from 0;
        print(3,str.indexOf("e"));
        print(4,str.charAt(3));
        print(5,str.codePointAt(2));
        print(6,str.replace("e","l"));
        print (7,str.concat("!!"));


    }
    public static  void demoList(){
        List<String> stringList=new ArrayList<>(); // array list , it can resize it
        List<String> stringListB=new ArrayList<>();
        for(int i=10; i<15;i++){
            stringList.add(String.valueOf(i));
        }
        for(int i=2;i<7;i++){
            stringListB.add(String.valueOf(i*i));
        }
        stringList.addAll(stringListB);
        print(1,stringList);
        print(2,stringList.get(3));
        Collections.sort(stringList);  //the raw data changed
        print(3,stringList); //as  string, it will be divide,so it's not  the number sort;
        Collections.sort(stringList, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o2.compareToIgnoreCase(o1); //use the string method
            }
        });
        print(4,stringList);
        print(5,stringList.remove(4)); //remove use index
        Collections.sort(stringList, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o2.compareTo(o1);
            }
        });
        print(6,stringList);
    }
    public  static void demoKeyValue(){
        Map<String,String> stringMap=new HashMap<>();
        for(int i=1;i<5;i++){
            stringMap.put(String.valueOf(i),String.valueOf(i*i)); //the mthod is put
        }
        print(1,stringMap);
        print(2,stringMap.entrySet());
        print(3,stringMap.keySet());
        print(4,stringMap.replace("2","A"));
        print(5,stringMap);
    }
    public static void demoException(String str1){
        try {
            int str2=str1.indexOf(22); //index和charset；

        }
        catch(Exception e){
            //the code catch the exception ,but don't throw it ,so the method don't to handle it
            e.printStackTrace();// it can tell you where the bug is;
            print(3,"something is wrong");
        }
        finally {
            System.out.println("this is not necessary");
        }
    }
    public static void  demoException02(int[] arrayInt) throws Exception{  //the varaible is array

        try{
            //noSuchMethod();
            int a=arrayInt[20]; //out of boundary
        }
        catch (Exception e){
            throw new Exception("new exception"); //the  method don't handle the exception,throw it,the method throws it
        }
    }
    public static void demoCommon(){
        Random random=new Random();
        random.setSeed(1);// use a formula or expression
        for(int i=0;i<4;i++){
            print(1,random.nextInt(100));
        }
        Date date=new Date();
        print(5,date);
        print(6,date.getTime()); //the unit is second
        DateFormat df=new SimpleDateFormat("YY-MM-DD hh:mm:ss");
        DateFormat df1=new SimpleDateFormat("yyyy-mm-dd hh:mm:ss"); //the difference of M and m
        print(7,df.format(date));
        print(8,df1.format(date));
        print(9,DateFormat.getDateInstance(DateFormat.FULL).format(date)); //use factory to produce  a dateFormat object;
        print(10,UUID.randomUUID());
        print(11,Math.nextDown(323.323));
    }
    public static void main(String[] args) throws Exception {
        System.out.println("this the foundation of China");
        print(2,4==4);
        print(33,"sdk");
        //demoString();
        //demoList();
        //demoKeyValue();
        demoException(null);
       // int[] arr=new {123,32}; mistake
        int[] arr1;  //just a declare
        int[] arr=new int[]{122,33}; //  from the test,the array is reference varible
        int leg=args.length;
        int leg01=arr.length;
       // demoException02(arr); //method out
        demoCommon();
    }

}
