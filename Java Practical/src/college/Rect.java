package college;

import java.util.Scanner;

public class Rect {
	int l = 20, b = 40; 
}

class area_rect extends Rect {
	int l=50, b = 60, p,a ;
	void add()
	{
		p = 2 * (super.l + super.b);
		System.out.println("Perimeter of rectangle :" +p);
		
		a =this.l * this.b;
		System.out.println("Area of rectangle :" +a);
				
	}
public static void main(String[] args) 
{
	area_rect a = new area_rect();
	a.add();
	}

}
