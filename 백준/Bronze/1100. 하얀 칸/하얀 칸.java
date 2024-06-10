import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[][] board= new String[8][8];
        
        for (int i=0; i<8; i++){
            board[i]=br.readLine().split("");
        }
        
        
        int answer=0;
        
        for (int i=0; i<8; i++){
            for (int j=0; j<8; j++){
                if ((i+j)%2==0 && board[i][j].equals("F")){
                    answer++;
                }
            }
        }
        System.out.println(answer);
        
    }
}