package college;

import java.util.Scanner;

import javax.imageio.IIOException;

public class Practical_throw {
	
		void age(int age) throws IIOException{
		if(age<=17) {
		throw new IIOException("age is not valid to vote");
		}
		else {
		System.out.println("welcome to vote");
		}
		}
		public static void main(String[] args) {
		Practical_throw obj=new Practical_throw();
		try {
		obj.age(18);
		} catch (IIOException e) {
		e.printStackTrace();
		}
		}
		
}
