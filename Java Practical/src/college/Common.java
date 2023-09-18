package college;

public class Common {
	
	  public static void main(String[] args) {
	    int[] arr1 = {3, 10, 1, 0, 9};
	    int[] arr2 = {32, 5, 10, 6, 9, 1};
	    for(int i = 0; i < arr1.length; i++){
	      for(int j = 0; j < arr2.length; j++){
	        if(arr1[i] == arr2[j]){
	          System.out.print(arr1[i] + " ");
	          break;
	        }
	      }
	    }
	  }
	}
