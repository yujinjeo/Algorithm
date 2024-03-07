import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
//import java.util.Arrays;

public class Main {
  
  public static void main(String[] args) throws IOException {
    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    String nk[]=br.readLine().split(" ");
    int n=Integer.parseInt(nk[0]);
    int k=Integer.parseInt(nk[1]);
    int values[]=new int[n];
    for (int i=n-1; i>=0; i--){
      values[i]=Integer.parseInt(br.readLine());
    }
    int ans=0;
    for (int i=0; i<n; i++){
      if (k==0)
        break;
      if ((int)(k/values[i])>0){
        ans+=(int)(k/values[i]);
        k%=values[i];
      }
    }
    System.out.print(ans);
    
  }

}