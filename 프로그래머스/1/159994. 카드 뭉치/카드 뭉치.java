class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "";
        int c1=0;
        int c2=0;
        
        for (String word : goal){
            if (c1<cards1.length && cards1[c1].equals(word)){
                c1++;
            }else if (c2<cards2.length && cards2[c2].equals(word)){
                c2++;
            }else{
                answer="No";
                break;
            }
        }
        
        if (!answer.equals("No")){
            answer="Yes";
        }
        
        return answer;
    }
}