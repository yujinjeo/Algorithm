class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        
        for(int i=0; i<targets.length; i++){
            String target=targets[i];
            int cnt =0;
            
            for (char c : target.toCharArray()){
                int cand=Integer.MAX_VALUE;
                int keyidx=0;
                for (int j=0; j<keymap.length; j++){
                    int thiskeyc=0;
                    if (keymap[j].contains(String.valueOf(c))){
                        thiskeyc=keymap[j].indexOf(c);
                        int ccnt=(thiskeyc)%keymap[j].length()+1;
                        if(ccnt<cand) cand=ccnt; 
                    }
                }
                if (cand>=101){
                    answer[i]=-1;
                }
                else{
                    cnt+=cand;
                    System.out.println(c);
                    System.out.println(cand);
                    System.out.println("---------");
                }
                
            }
            if (answer[i]!=-1){
                answer[i]=cnt;
            }
            
            
        }
        
        
        
        return answer;
    }
}