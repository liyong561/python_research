package utilTest;

import java.util.Timer;
import java.util.TimerTask;

public class TimerTest {
    static  Timer timer=new Timer(); //what's the use of timer?timer的意义在于可以通过方法，定时的执行任务；
    static TimerTask timerTask=new TimerTask() { // this is abstract class,所以需要这样的实现。
        int i=0;
        @Override
        public void run() {
            if(i>5){
                this.cancel();
            }
            System.out.println("this is a timer task");
            i++;

        }
    } ;
    public static void main(String[] args) {
        timer.schedule(timerTask,1000,1000*3);

    }

}
