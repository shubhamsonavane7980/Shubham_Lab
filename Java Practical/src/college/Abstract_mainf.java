package college;


abstract class Abstract_class
{
	abstract int display(int b, String a);
}
public class Abstract_mainf extends Abstract_class  {
	int display(int b, String a) {
		System.out.println("WELCOME " +a+ "  " +b);
		return b;
	}
	public static void main(String[] args) {
		Abstract_mainf ab = new Abstract_mainf();
		ab.display(0,  "World");
	}
}
