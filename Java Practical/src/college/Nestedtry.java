package college;

public class Nestedtry {
    public static void main(String[] args) {  
           try{    
                int a[]= {15,25,35,45,55};    
                System.out.println(a[5]);  
                try{
                int x = a[2]/0;
                }catch(ArithmeticException e)   {  
	               System.out.println("Arithmetic Exception occurs");  
	               }    
           }
           catch(ArrayIndexOutOfBoundsException e)  
           {  
            System.out.println("ArrayIndexOutOfBounds Exception occurs");  
            System.out.println("Element at such index does not exists");
           }    
    }
 
}
