import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    String nums[]=br.readLine().split(" ");
    br.close();
    int h=Integer.parseInt(nums[0]);
    int m=Integer.parseInt(nums[1]);

    if (m>=45){
      System.out.println(h+" "+(m-45));
      return;
    }else{
      m=(60+m)-45;
      if (h==0)
        h=23;
      else
        h-=1;
      System.out.println(h+" "+m);
      return;
    }
    
  }

}