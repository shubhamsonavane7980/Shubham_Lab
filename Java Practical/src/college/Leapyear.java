package college;

import java.util.Scanner;

public class Leapyear {
	
	public static void main(String[] args) {
	
	int year;
	System.out.println("Enter an year: ");
	Scanner scanner = new Scanner(System.in);
	year = scanner.nextInt();
	
	if(((year % 4 == 0) && (year % 100 !=0 )) || (year % 400 == 0)) {
		System.out.print("Specified year is a leap year ");
	}else {
		System.out.print("Specified year is a not leap year ");
	}
	
	
	
	}

}
