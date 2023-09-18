package college;

class Combine1 {
	
	protected String name="hello world";
	protected void display() {
	System.out.println("college package");
	System.out.println(name);
	}
}



public class Combine2 extends Combine1{
public static void main(String[] args) {
Combine2 obj=new Combine2();
obj.display();
}
}	
