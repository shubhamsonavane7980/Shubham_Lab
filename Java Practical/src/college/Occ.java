package college;

public class Occ {
	public static void main(String[] args) {
		int a[] = {5,15,25,35,45,55,65,75,85};
		int val = 5;
		int count = 0;
		int copy[] = new int [a.length];
		for (int i =0; i<a.length; i++ ) {
			if (val != a[i]) {
				copy[i] = a[i];
			}
		}
		for (int k =0; k<a.length; k++) {
			System.out.print(copy[k]  +" ");
		}
	}
}
