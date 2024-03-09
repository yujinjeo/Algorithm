import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
  public static void main(String[] args) throws IOException{
    //입력 받기
    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    String board[]=new String[5];
    int maxl=0;
    for(int i=0; i<5; i++){
      String input=br.readLine();
      maxl=Math.max(maxl,input.length());
      board[i]=input;
    }
    for (int i=0; i<5; i++){
      for (int j=board[i].length(); j<maxl; j++){
        board[i]+="*";
      }
    }

    //세로로 읽기
    for(int i=0; i<maxl; i++){
      for(int j=0; j<5; j++){
        if (board[j].charAt(i)!='*')
          System.out.print(board[j].charAt(i));
      }
    }
    
  
  }
  
}