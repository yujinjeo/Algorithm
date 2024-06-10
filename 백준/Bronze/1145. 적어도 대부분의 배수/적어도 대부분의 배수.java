import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] str=br.readLine().split(" ");
        int [] lst = new int[5];
        
        for (int i=0; i<5; i++){
            lst[i]=Integer.parseInt(str[i]);
        }
        
        int n=1;
        
        
        while(true){
            int cnt=0;
            for (int i=0; i<5; i++){
                if(n%lst[i]==0){
                    cnt++;
                }
            }
            if(cnt>=3){
                break;
            }else{
                n++;
            }
            
        }
        
        System.out.println(n);
        
        

        
    }
}