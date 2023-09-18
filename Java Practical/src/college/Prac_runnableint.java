package college;

public class Prac_runnableint implements Runnable {
	
	public void run() {
	System.out.println("Implements Runnable");
	}
	public static void main(String[] args) {
	Prac_runnableint obj=new Prac_runnableint();
	Thread t1=new Thread(obj);
	t1.start();
	}
	
}
