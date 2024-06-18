import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        int n = score.length;
        List<Integer> lst = new ArrayList<Integer>();
        for (int a:score){
            lst.add(a);
        }
        
        Collections.sort(lst,Collections.reverseOrder());
        
        int idx=m-1;
        
        while(n>idx){
            int o = lst.get(idx);
            answer+=o*m;
            idx+=m;      
        }
        
        return answer;
    }
}