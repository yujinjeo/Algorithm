import java.util.*;

class Solution {
    public int[] solution(String[] wallpaper) {
        List<Integer> xloc = new ArrayList<Integer>();
        List<Integer> yloc = new ArrayList<Integer>();
        
        for (int i=0; i<wallpaper.length; i++){
            for (int j=0; j<wallpaper[0].length(); j++){
                if(wallpaper[i].charAt(j)=='#'){
                    xloc.add(i);
                    yloc.add(j);
                }
            }
        }
        
        int xmin= Collections.min(xloc);
        int ymin = Collections.min(yloc);
        int xmax = Collections.max(xloc)+1;
        int ymax = Collections.max(yloc)+1;
        
        int [] answer={xmin, ymin, xmax, ymax};

        
        return answer;
    }
}