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
    public static List<String> sort(List<String> ls){
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

      return  null;
    }

    public static void main(String[] args) {
        List<String> ls=split(read("E:/TestFile/a.txt"));
        System.out.println(ls);

    }
}
