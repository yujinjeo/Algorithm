class Solution {
    public static void move(String[] park,String route, int[] loc){
        char dir=route.charAt(0);
        int cnt=Character.getNumericValue(route.charAt(2));
        
        int n=park.length;
        int m=park[0].length();
        
        if (dir == 'E'){
            if(loc[1]+cnt<m){ 
                int flag=0;
                for (int i=1; i<=cnt;i++){
                    if(park[loc[0]].charAt(loc[1]+i)=='X') flag=1;
                }
                if(flag==0){
                    loc[1]+=cnt;
                }
            }
        }
        else if (dir== 'W'){
            if(loc[1]-cnt>=0) {
                int flag=0;
                for (int i=1; i<=cnt;i++){
                    if(park[loc[0]].charAt(loc[1]-i)=='X') flag=1;
                }
                if(flag==0){
                    loc[1]-=cnt;
                }
            }
        }
        else if (dir == 'N'){
            if(loc[0]-cnt>=0) {
                int flag=0;
                for (int i=1; i<=cnt;i++){
                    if(park[loc[0]-i].charAt(loc[1])=='X') flag=1;
                }
                if(flag==0){
                    loc[0]-=cnt;
                }
            }
        }
        else if (dir=='S'){
            if (loc[0]+cnt<n) {
                int flag=0;
                for (int i=1; i<=cnt;i++){
                    if(park[loc[0]+i].charAt(loc[1])=='X') flag=1;
                }
                if(flag==0){
                    loc[0]+=cnt;
                }
            }
        }
        
        
    }
    
    
    public int[] solution(String[] park, String[] routes) {
        int[] answer = {};
        int [] loc = new int[2];
        int flag=0;
        for (int i=0; i<park.length; i++){
            for (int j=0; j<park[0].length(); j++){
                if(park[i].charAt(j)=='S'){
                    loc[0]=i;
                    loc[1]=j;
                    flag=1;
                    break;
                }
            }
            if(flag==1){
                break;
            }
        }
        
        for(int i=0; i<routes.length; i++){
            move(park,routes[i], loc);
        }
        
        answer=loc;
        
        return answer;
    }
}