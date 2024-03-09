import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
  public static void main(String[] args) throws IOException{
    //입력 받기
    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    int n=Integer.parseInt(br.readLine());
    int board[][]=new int[100][100];
    int x=0;
    int y=0;
    int ans=0;
    for (int i=0; i<n; i++){
      String tmp[]=br.readLine().split(" ");
      x=Integer.parseInt(tmp[0]);
      y=Integer.parseInt(tmp[1]);
      for(int k=x;k<x+10;k++){
        for(int t=y;t<y+10;t++){
          board[k][t]=1;
        }
      }
    }
    for (int i=0;i<100;i++){
      for(int j=0; j<100; j++){
        if (board[i][j]==1)
          ans+=1;
      }
    }
    
    System.out.println(ans);
  }
  
}