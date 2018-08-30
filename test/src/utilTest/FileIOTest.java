package utilTest;

import java.io.*;

public class FileIOTest {
    /**
     *  将字符串写入文件
     * @param content
     */
    public static void write(String filePath,String content) {
        FileWriter fileWriter_xls;
        FileWriter fileWriter_txt;
        try {
            fileWriter_xls = new FileWriter(filePath); // 路径不存在就会报错，且文件后缀名真的有效
            fileWriter_txt = new FileWriter("E:\\TestFile\\b.xlsx", true);//使用append模式。
            fileWriter_xls.write(content);  //并不是这样就完了，还要到内存中
            fileWriter_xls.flush();
            fileWriter_xls.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     *  将制定文件读入内存的字符串。
     * @param fileName
     * @return
     */
    public static String read(String fileName) {
        FileReader fileReader_txt;
        File file1 = new File(fileName);
        Long length = file1.length();
        String content = null;
        try {
            char[] chars = new char[length.intValue()]; //以1024为读取单位,以文件长度为单位，或者先把内容以字节的方式读取出来。
            fileReader_txt = new FileReader(file1);
            fileReader_txt.read(chars); //只能读取char数组
            content = new String(chars);
           // System.out.println("内容：" +content);内容都变成乱码了
            System.out.println("内容：");
            System.out.println(content);

        } catch (Exception e) {
            e.printStackTrace();
        }
        return content;
    }
    /**
     * 使用缓冲流对文件流进行包装，缓冲流的方法更多，也跟高效
     * @param fileName
     * @return
     */
    public static String readBuffer(String fileName){
        FileReader fileReader;
        BufferedReader bufferedReader;
        StringBuffer content=new StringBuffer();//content=null;StringBuffer对象要使用new创建一个对象。
        try {
             fileReader = new FileReader(fileName);
             bufferedReader=new BufferedReader(fileReader);
             String line;
             while ((line=bufferedReader.readLine())!=null){  //使用逐行读取的方法，判读是否读完。
                 content.append(line);
             }

        }catch (Exception e){
            e.printStackTrace();
        }
        String str=new String(content);
        return str;
    }
    public static String readStream(String fileName){
        File file=new File(fileName);
        Long length=file.length();
        System.out.println("文件长度："+length);
        byte[] bytes=new byte[length.intValue()];
        FileInputStream fis;
        String str=null;
        try{
            fis=new FileInputStream(file);
            fis.read(bytes); //一次性读完
            str=new String(bytes,"utf-8");
        }catch (Exception e){
            e.printStackTrace();
        }

        return  str;
    }


    public static void main(String[] args) {
        write("E:/TestFile/a.txt","I love programming,I can make a difference,黎勇一定要多努力，硕士阶段不能荒废，不管是什么语言，都是character");
        // read("F:\\专业学习资料\\javaEE学习\\JavaEE教程.pdf");
        read("E:\\学习生活文件\\学习笔记\\java学习.docx");
        //readBuffer("E:\\学习生活文件\\学习笔记\\java学习.docx");
        System.out.println(readStream("F:\\专业学习资料\\javaEE学习\\JavaEE教程.pdf"));
    }
}
