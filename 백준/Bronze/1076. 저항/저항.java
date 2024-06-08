import java.util.*;

public class Main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args)
    {
        
        Map<String, List<Integer>> table = new HashMap<>(){{
            put("black",Arrays.asList(0,1));
            put("brown",Arrays.asList(1, 10));
            put("red",Arrays.asList(2, 100));
            put("orange",Arrays.asList(3, 1000));
            put("yellow",Arrays.asList(4, 10000));
            put("green",Arrays.asList(5,100000));
            put("blue",Arrays.asList(6,1000000));
            put("violet",Arrays.asList(7,10000000));
            put("grey",Arrays.asList(8,100000000));
            put("white",Arrays.asList(9,1000000000));
        }};
        
        
        Scanner sc = new Scanner(System.in);
        String first = sc.next();
        String second = sc.next();
        String last = sc.next();
        
        
        int val1 = table.get(first).get(0)*10;
        int val2= table.get(second).get(0);
        int val3 = table.get(last).get(1);
        
        long answer = (val1+val2)*(long)val3;
        
        System.out.println(answer);
        
        


    }
}
