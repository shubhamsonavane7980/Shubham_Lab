package college;

import java.util.Scanner;

public class Simpleinterest {

	public static void main(String[] args) {
		float p,r,t,sinterest;
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter the principal: ");
		p = scan.nextInt();
		System.out.print("Enter the Rate of Interest: ");
		r = scan.nextInt();
		System.out.print("Enter the Time Period: ");
		t = scan.nextInt();
		sinterest = (p*r*t)/100;
		System.out.print("Simple Interest is = " +sinterest);
	}
}
