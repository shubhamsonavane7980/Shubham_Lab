package college;

public class Copy_array {
	
	public static void main(String args[]){
	int a[]={10,20,30,40,50,60,70};
	int b[]=new int[a.length];
	//copying one array to another
	for(int i=0;i<a.length;++i){
	b[i]=a[i];
	}
	
	for(int j=0;j<b.length;j++){
	System.out.print(b[j]+" ");
	}
	}
	
}
