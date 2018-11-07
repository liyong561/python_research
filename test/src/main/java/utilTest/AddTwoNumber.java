package utilTest;

public class AddTwoNumber {
    public static void main(String[] args) {
        ListNode l1=new ListNode(5);
        ListNode l2 =new ListNode(5);
        ListNode ls=addTwoNumbers(l1,l2);
        System.out.println(ls.next.val);
    }
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int flag = 0;
        ListNode q = new ListNode(-1);  //这个-1具有特殊的意义
        ListNode p=q;   //涉及到赋值问题,p的位置
        while (l1 != null && l2 != null) {  //判断是否为空
            int val = l1.val + l2.val + flag;
            flag = 0; //用完之后应该清零
            if (val > 9) {
                val = val % 10;
                flag = 1;
            }
            if (q.val == -1) { //使用了p，必须保证p为非空,先判空吧
                q.val = val;
                // p=q.next; //把一个null赋值给p，有点搞笑。
            } else {
                ListNode ls = new ListNode(val);
                p.next = ls;
                p = p.next;  //是p还是p.next是一个问题
            }
            l1 = l1.next;
            l2 = l2.next;
        }  //[8],[8],这种问题还是不能解决。等长和不等长的问题
        while (l1 != null) {
            int val = l1.val + flag;  //直接操作对象属性,/解决最后一位进位的问题
            flag = 0;
            if (val > 9) {
                l1.val = 0;
                flag = 1;
                l1.next = l1;
            } else {
                l1.val = val;
            }
            p = l1;
            l1 = l1.next;
        }
        while (l2 != null) {
            int val = l2.val + flag;  //可能要进位，就是说要考虑全面
            flag = 0;
            if (val > 9) {
                l2.val = 0;
                flag = 1;
            } else {
                l2.val = val; //这句话不能少
            }
            p=l2;       //那就保证p每次都不为null
            l2 = l2.next;
        }
        if (flag == 1) {
            ListNode ls = new ListNode(1);
            if(p==null){

            }
            p.next = ls; //
            System.out.println(p.val);
            //System.out.println("dfdf");
             int a=(int)5343.42;
        }
        return q;
    }
}

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }   //还有两个列表长度不等的情况
}
