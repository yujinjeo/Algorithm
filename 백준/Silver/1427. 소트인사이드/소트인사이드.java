import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
//import java.util.Arrays;

public class Main {
  
  public static void main(String[] args) throws IOException {
    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    String tmp[]=br.readLine().split("");
    int nums[]=new int[tmp.length];
    for (int i=0; i<tmp.length; i++){
      nums[i]=Integer.parseInt(tmp[i]);
    }

    for (int i=0; i<nums.length-1; i++){
      int maxval=i;
      for (int j=i+1; j<nums.length; j++){
        if (nums[maxval]<nums[j]){
          maxval=j;
        }
      }
      int temp=nums[i];
      nums[i]=nums[maxval];
      nums[maxval]=temp;

      System.out.print(nums[i]);
      
    }
    System.out.print(nums[nums.length-1]);
  }

}