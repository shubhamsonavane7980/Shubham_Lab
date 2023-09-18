package college;

class interthread {
	int amount = 10000;
	synchronized void withdraw(int amount) {
		System.out.println("Going to withdraw");
		if (this.amount<amount) {
			System.out.println("Less balance; Waiting for Deposit");
		try {
			wait();
		}catch(Exception e){}
		}
	
	this.amount -= amount;
	System.out.println("Withdraw Completed");
	}
	synchronized void deposit(int amount) {
		System.out.println("Going to Deposit");
		this.amount += amount;
		System.out.println("Deposit Completed");
		notify();
	}
}
public class Interthread1
{
	public static void main(String[] args) {
		final interthread c = new interthread();
		new Thread()
		{
			public void run() {
				c.withdraw(15000);
			}
		}.start();
		new Thread() {
			public void run() {
				c.deposit(15000);
			}
		}.start();
	}	
}
