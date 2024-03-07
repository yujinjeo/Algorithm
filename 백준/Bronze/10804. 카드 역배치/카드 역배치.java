import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
  
  public static void main(String[] args) throws IOException {
    int cards[]=new int[21];
    for (int i=0; i<21; i++){
      cards[i]=i;
    }
    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    for (int i=0; i<10; i++){
      String tmp[]=br.readLine().split(" ");
      int s=Integer.parseInt(tmp[0]);
      int e=Integer.parseInt(tmp[1]);

      int gap=e-s;
      int start=s;
      int end=e;
      while(gap>0){
        int temp=cards[start];
        cards[start]=cards[end];
        cards[end]=temp;

        start+=1;
        end-=1;
        gap-=2;
      }
      
    }
    for(int j=1; j<21; j++){
      System.out.print(cards[j]+" ");
    }
    
  }

}