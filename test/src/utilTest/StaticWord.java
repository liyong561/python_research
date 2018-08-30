package utilTest;

import java.io.File;
import java.io.FileReader;
import java.util.*;

public class StaticWord {
    /**
     * 将输入的文件内容转换为一个大的字符串。FileInputStream主要用于输入非字符的数据，如图片，在此处并不合适。
     * 应该使用FileWriter或者FileReader更合适一些。
     * @param file
     * @return
     */
    public static String  read(String file) {
        FileReader fr;
        File file1;
        Long length;
        char[] chars=null;
        try {
            file1=new File(file);
            length=file1.length();
            chars=new char[length.intValue()];
            fr = new FileReader(file1);
            fr.read(chars);

        }
        catch (Exception e){
            e.printStackTrace();
        }
        String str=new String(chars);
       return  str;
    }

    /**
     * 将单词一个个的放进list，后续数据处理使用。
     * @param content
     * @return
     */
    public static List<String> split(String content){
        String[] strs=content.split("[^a-zA-Z]+"); //正则表达式，就是这么强大。
        //https://stackoverflow.com/questions/14079277/uva-494-regex-a-za-z-to-split-words-using-java 会出现空元素
        List<String> ls=new ArrayList<>(Arrays.asList(strs));
        ls.removeAll(Collections.singleton("")); //剔除空元素，null不行，空元素和null元素的区别。singleton:顾名思义，是单元素列表。
        return ls;
    }

    /**
     * 按照单词出现的频率高低返回列表，这是一个排序过程。
     * @param ls
     * @return
     */
    public static Map<String,Integer> sort(List<String> ls){
        Map<String,Integer> map=new HashMap<>();
        for(String str:ls){
            if(map.containsKey(str)){
                Integer num=map.get(str);
                num++;
                map.replace(str,num);
            }
            else {
                map.put(str,1);
            }
        }
        List<Map.Entry<String,Integer>> ls_sort=new ArrayList<>(); //map.Entry<String,Integer>，Entry是Map的静态内部类，
        ls_sort.addAll(map.entrySet());
        ls_sort.sort(  //java中可以向一个函数传入什么？java对象，然后就可以重写其中的方法，如果只有一个函数，就用lamda表达式。
                new Comparator<Map.Entry<String, Integer>>() {
                    @Override
                    public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
                        return o1.getValue().compareTo(o2.getValue());  //o1.getValue().compareTo(o2.getValue()),返回正数则前者大。
                    }
                }
        ); //调用对象的sort方法，只要告诉系统怎么排序就可以了。
        Map<String,Integer> map1=new LinkedHashMap<>(); //此处不应该使用HashMap,否则输出顺序不对。
        for (Map.Entry<String,Integer> ele:ls_sort){
            map1.put(ele.getKey(),ele.getValue());
        }
      return  map1;
    }
    public static  List<Integer> array_sort(Integer[] array_integer){
        Arrays.sort(array_integer);
        //System.out.println(array_integer);
        List<Integer> ls=Arrays.asList(array_integer);
;       Collections.sort(ls);  //默认是升序。
        System.out.println(ls);
        return  ls;
    }

    public static void main(String[] args) {
        array_sort(new Integer[]{1,23,5,9});
        List<String> ls=split(read("E:/TestFile/a.txt"));
        System.out.println(ls);
        Map<String,Integer> map=sort(ls);
        System.out.println(map);

    }
}
