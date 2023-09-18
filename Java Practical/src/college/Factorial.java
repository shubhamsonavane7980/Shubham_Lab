package college;


import java.util.Scanner;

public class Factorial {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter the number: ");
		int n = sc.nextInt();
		int Fact = 1; 
		for(int i=1;i<=n;i++)
		{
			Fact =  Fact *i;
		}
		System.out.print("The factorial is: " +Fact);
		
	}
}
