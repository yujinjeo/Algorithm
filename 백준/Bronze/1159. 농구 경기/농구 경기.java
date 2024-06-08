import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] lst = new String[n];

        for (int i = 0; i < n; i++){
            lst[i] = sc.next();
        }
        Arrays.sort(lst);

        List<Character> answer = new ArrayList<>();
        char a = lst[0].charAt(0);
        int cnt = 1; // Initialize cnt to 1

        for (int i = 1; i < n; i++){
            if (lst[i].charAt(0) != a){
                if (cnt >= 5){
                    answer.add(a);
                }
                a = lst[i].charAt(0);
                cnt = 1; // Reset cnt to 1 for the new character
            } else {
                cnt++;
            }
        }

        // Check the last character group
        if (cnt >= 5){
            answer.add(a);
        }

        if (answer.isEmpty()){
            System.out.println("PREDAJA");
        } else {
            for (char k : answer){
                System.out.print(k);
            }
        }
    }
}
