import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] lst = br.readLine().split(" ");
        
        int x=Integer.parseInt(lst[0]);
        int y=Integer.parseInt(lst[1]);
        int w=Integer.parseInt(lst[2]);
        int h=Integer.parseInt(lst[3]);
        
        int answer=Integer.MAX_VALUE;
        
        answer = Math.min(Math.min(x,w-x), Math.min(y,h-y));
        System.out.println(answer);
        
    }
}