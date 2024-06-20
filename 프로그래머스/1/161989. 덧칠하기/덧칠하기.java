class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        boolean[] painted = new boolean[n];
        for (int s : section){
            painted[s-1]=true;
        }
        
        int i=0;
        while (i<n){
            if (!painted[i]) {i++; continue;}
            else {
                for (int j=i; j<(i+m>n?n:i+m) ;j++){
                    painted[j]=true;
                }
                answer+=1;
                i+=m;
            }
        }
        
        return answer;
    }
}