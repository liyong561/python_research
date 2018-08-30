package utilTest;

import java.lang.management.ManagementFactory;
import java.lang.management.ThreadInfo;
import java.lang.management.ThreadMXBean;

public class ThreadTest {

    public static void main(String[] args) {
        ThreadMXBean threadMXBean= ManagementFactory.getThreadMXBean();  //管理系统的对象
        ThreadInfo[]  threadInfos=threadMXBean.dumpAllThreads(false,false);
        for (ThreadInfo threadInfo:threadInfos){
            System.out.println(threadInfo.getThreadId()+":"+threadInfo.getThreadName());
        }
    }
}
