import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
  public static void main(String[] args) throws IOException{
    //입력 받기
    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    char ans[]=new char[3];
    for(int i=0; i<3; i++){
      String tmp[]=br.readLine().split(" ");
      int cnt=0;
      for (int j=0; j<4; j++){
        if (tmp[j].equals("1"))
          cnt+=1;
      }
      switch(cnt){
        case 0:
          ans[i]='D';
          break;
        case 1:
          ans[i]='C';
          break;
        case 2:
          ans[i]='B';
          break;
        case 3:
          ans[i]='A';
          break;
        case 4:
          ans[i]='E';
          break;
      }
      
    }
    for (int i=0; i<3; i++)
      System.out.println(ans[i]);
  
  }
  
}