package utilTest;

import com.oracle.webservices.internal.api.databinding.DatabindingMode;
import lombok.AllArgsConstructor;
import lombok.Cleanup;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.hssf.usermodel.HSSFCell; //有两种模式可供选择。
import org.apache.poi.xssf.streaming.SXSSFWorkbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import lombok.Data;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * java读取excel文件使用了Apache的poi包,当然也有jxl可以用，但是那很旧了。
 */
public class ExcelFile {
    /**
     * 借助于现成的api，函数的设计思想并不复杂。
     *
     * @param file
     * @return
     */
    public static List<List<String>> readExcel(String file) {  //
        /**
         * The supplied data appears to be in the Office 2007+ XML. You are calling the part of POI that deals with OLE2 Office Documents.
         * You need to call a different part of POI to process this data (eg XSSF instead of HSSF)
         */
        List<List<String>> lists = new ArrayList<List<String>>();
        try {
            FileInputStream fis = new FileInputStream(file);
            //XSSFWorkbook workbook =new XSSFWorkbook(fis);  //FileReader参数不可以，HSSFWorkbook和XSSFWorkbook
            Workbook workbook = WorkbookFactory.create(fis);
            Sheet sheet = workbook.getSheetAt(0); //默认第一张表单
            for (Row row : sheet) {   //可以看到sheet对象就是Row对象的集合
                List<String> ls = new ArrayList<String>();
                for (Cell cell : row) {
                    cell.setCellType(CellType.STRING); //建议使用sheet，而不是hssfsheet
                    ls.add(cell.getStringCellValue()); //Cannot get a STRING value from a NUMERIC cell
                }
                lists.add(ls);
            }
            fis.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return lists;
    }

    /**
     * @param lists
     * @param file
     * @return
     */
    public static HSSFWorkbook createExcel(List<List<String>> lists, String[] fields, String file) {
        HSSFWorkbook wb = new HSSFWorkbook(); //创建工作薄，只是这个工作薄没有和文件关联
        Sheet sheet = wb.createSheet(); //get和create的差距。
        for (int i = 0; i < fields.length; i++) {
            sheet.setColumnWidth(i, 256 * 50); //256个单位大概为一个字符的宽度。
        }
        Row row = sheet.createRow(0); //表单的第一项,用于存放字段名。
        CellStyle cs = wb.createCellStyle();
        CellStyle cs1 = wb.createCellStyle(); //样式,一个用于列名行，一个用于数值行。

        Font font = wb.createFont();
        Font font1 = wb.createFont();// 字体

        cs.setAlignment(HorizontalAlignment.CENTER);
        cs.setFillBackgroundColor((short) 230);

        font.setColor((short) 29);
        font.setFontHeight((short) 89);

        font1.setColor((short) 54); //字体颜色
        font1.setFontHeightInPoints((short) 56); //宽度

        cs.setFont(font);
        cs1.setFont(font1);
        for (int i = 0; i < fields.length; i++) {
            row.createCell(i).setCellStyle(cs);
            row.getCell(i).setCellValue(fields[i]);
        }
        /**
         int i=1;
         for(List<String> list:lists){
         Row row1=sheet.createRow(i);
         for (String str:list){
         row1.getCell()
         }
         i++;
         }*/
        for (int i = 0; i < lists.size(); i++) {
            List<String> ls = lists.get(i);
            Row row1 = sheet.createRow(i + 1);
            for (int j = 0; j < ls.size(); j++) {
                row1.createCell(j).setCellValue(ls.get(j));
                row1.getCell(j).setCellStyle(cs1);
            }
        }

        try {
            FileOutputStream fos = new FileOutputStream(file);
            wb.write(fos);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return wb;
    }

    public static void createExcelWithNoCss(List<List<String>> lists, String[] fields, String file) {
        Workbook wb =new XSSFWorkbook(); //WorkbookFactory只使用于读取excel;
        Sheet sheet = wb.createSheet(); //get和create的差距。
        for (int i = 0; i < fields.length; i++) {
            sheet.setColumnWidth(i, 256 * 50); //256个单位大概为一个字符的宽度。
        }
        Row row = sheet.createRow(0); //表单的第一项,用于存放字段名。
        for (int i = 0; i < fields.length; i++) {
            row.createCell(i).setCellValue(fields[i]);
        }

        for (int i = 0; i < lists.size(); i++) {
            List<String> ls = lists.get(i);
            Row row1 = sheet.createRow(i + 1);
            for (int j = 0; j < ls.size(); j++) {
                row1.createCell(j).setCellValue(ls.get(j));

            }
        }
        try {
            FileOutputStream fos = new FileOutputStream(file);
             wb.write(fos);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     *  从excel中读取对象列表，这些都不难，具备基本的思维方式就可以了。
     * @param file
     * @return
     */
    public static  List<Student> readObject(String file) throws Exception{
        FileInputStream fis=new FileInputStream(file);
        Workbook wb=WorkbookFactory.create(fis);  //这个方法也会抛出异常
        Sheet sheet=wb.getSheetAt(0);
        List<Student> ls=new ArrayList<>();
        for(int i=1;i<sheet.getLastRowNum()+1;i++){
              Row row=sheet.getRow(i); //变量驱动，因为其结构一样。
              Cell cell;        //标准的字段赋值操作，省略不了
              cell=row.getCell(0);
              cell.setCellType(CellType.STRING);
              String name=row.getCell(0).getStringCellValue();
              cell=row.getCell(1);
              cell.setCellType(CellType.STRING);
              int  age=Integer.parseInt(row.getCell(1).getStringCellValue());
              cell=row.getCell(2);
              cell.setCellType(CellType.STRING);
              String school=row.getCell(2).getStringCellValue();
              Student student=new Student(name,age,school);
              ls.add(student);
        }
        return ls;
    }
    public  static  void writeExcelObject(List<Student> ls,String[] fields,String file){
        //List可以成千上万，也可以上亿，多的可以使用分片，就像中国人口分区一样。
        Workbook wb=new SXSSFWorkbook();
        try{
             Sheet sheet=wb.createSheet("sheet1");
             Row row=sheet.createRow(0);
             for(int i=0;i<fields.length;i++){
                 Cell cell=row.createCell(i,CellType.STRING);
                 cell.setCellValue(fields[i]);
             }
             for(int i=1;i<ls.size()+1;i++){
                 row=sheet.createRow(i);
                 Student student=ls.get(i-1);

                 Cell cell=row.createCell(0,CellType.STRING);
                 cell.setCellValue(student.name);

                 cell=row.createCell(1,CellType.STRING);
                 cell.setCellValue(student.age);

                 cell=row.createCell(2,CellType.STRING);
                 cell.setCellValue(student.school);
             }
             FileOutputStream fis=new FileOutputStream(new File(file));
             wb.write(fis);
        }catch (Exception e){
            e.printStackTrace();
        }
    }
    public static void main(String[] args) throws Exception {
        List<List<String>> lists = readExcel("E:/TestFile/a.xlsx");
        List<Student> list=readObject("E:/TestFile/a.xlsx");
        Student student=list.get(0);
        System.out.println(student);
        List<String> fieldsList = lists.remove(0);
        //String[] fields=new String[];缺少数组维数。
        int len = lists.get(0).size();
        String[] fields = new String[len];
        fieldsList.toArray(fields);
        String file = "E:/TestFile/a1.xlsx";
        String file1="E:/TestFile/a2.xlsx";
        createExcel(lists, fields, file);
        writeExcelObject(list, fields, file1);
    }
}
    @Data
            /**
             * Student不应该定义在public class 类中。
             */
    class  Student{
        public Student() {
        }

        public Student(String name, int age, String school) {
            this.name = name;
            this.age = age;
            this.school = school;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public int getAge() {
            return age;
        }

        public void setAge(int age) {
            this.age = age;
        }

        public String getSchool() {
            return school;
        }

        public void setSchool(String school) {
            this.school = school;
        }

        String name;
        int age;
        String school;

}