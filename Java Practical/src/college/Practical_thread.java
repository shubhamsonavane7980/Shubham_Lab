package college;

public class Practical_thread extends Thread{
	public void run() {
		for (int i=0;i<=5;i++)
		{
			System.out.println(i+": hello World");
		}
	}
	public static void main(String[] args) {
		Practical_thread a = new Practical_thread();
		a.start();
		for (int j=0;j<=5;j++)
		{
			System.out.println(j+": New World");
		}
	}
}
