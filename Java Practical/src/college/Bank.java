package college;


public class Bank {

	
		String name;
		float bal;
		String account_type;
		Bank( String name,float bal,String account_type){
		this.name=name;
		this.bal=bal;
		this.account_type=account_type;
		}
		public String getName() {
		return name;
		}
		public void setName(String name) {
		this.name = name;
		}
		public float getBal() {
		return bal;
		}
		public void setBal(float bal) {
		this.bal = bal;
		}
		public String getAccount_type() {
		return account_type;
		}
		public void setAccount_type(String account_type) {
		this.account_type = account_type;
		}
		}
		class Account extends Bank{
		Account(String name, float bal, String account_type) {
		super(account_type, bal, account_type);
		}
		public void witdraw(int amt) {
		if(super.bal>=amt) {
		float withdraw=super.bal-amt;
		super.setBal(withdraw);
		System.out.println("amout reaming after withdraw " +getBal());
		}else {
		System.out.println("low balance");
		}
		}
		public void deposite(int amt) {
		float deposite= super.bal+amt;
		super.setBal(deposite);
		System.out.println(getBal());
		}
		public static void main(String[] args) {
		Account obj= new Account("RAM", 5000, "saving");
		obj.witdraw(500);
		obj.deposite(5000);
		}
		

}
