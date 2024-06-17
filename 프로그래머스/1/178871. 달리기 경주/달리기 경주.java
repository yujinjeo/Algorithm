import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = {};
        // list 의 indexOf도 시간이 많이 걸린다. 이중 반복문을 쓰지 않고 단일 반복문으로 순서를 바꿀 수 있어야 한다. 그러기 위해 Map을 사용해서 순서를 저장하려는것.
        
        Map<String, Integer> lst = new HashMap<String ,Integer> ();
        int ii=0;
        for (String val : players){
            lst.put(val,ii++);
        }

        for (String call : callings){
            int idx=lst.get(call);
            
            lst.put(players[idx],idx-1);
            lst.put(players[idx-1],idx);
            String tmp=players[idx-1];
            players[idx-1]=call;            
            players[idx]=tmp;
            
        }
        
        answer=players;
        
        return answer;
    }
}