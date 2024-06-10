import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            
        String n = br.readLine();  // Read the input string
        if(n.equals("0")){
            System.out.println(n);
            
        }else{
            
            String[] lst = {"000","001","010","011","100","101","110","111"};
        
            String[] l = n.split("");
            
            StringBuilder sb = new StringBuilder();
            
            String answer="";
            
            for (int i=0; i<l.length; i++){
                int t= n.charAt(i)-'0';
                sb.append(lst[t]);
                
            }
            
            int idx=0;
            answer=sb.toString();
            
            while(true){
                if(answer.charAt(idx)!='1'){
                    idx++;
                }else{
                    break;
                }
            }
        
            System.out.println(answer.substring(idx));
            
        }
        
        
        
        
        
        
    }
}