import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int m=sc.nextInt();
        int sixp=1001;
        int onep=1001;
        
        
        for (int i=0; i<m; i++){
            int a=sc.nextInt();
            int b=sc.nextInt();
            
            if(sixp>a){
                sixp=a;
            }
            if(onep>b){
                onep=b;
            }
            
        }
        
        int price=0;
        int pricek = Integer.MAX_VALUE;
        if(n%6>=1){
            price=((int)(n/6)+1)*sixp;
            pricek=((int)(n/6))*sixp+(n%6)*onep;
        }else{
            price=((int)(n/6))*sixp;
        }
        price=Math.min(price,pricek);
        
        
        
        if(price>n*onep){
            price =n*onep;
        }
        System.out.println(price);
        
        
    }
}