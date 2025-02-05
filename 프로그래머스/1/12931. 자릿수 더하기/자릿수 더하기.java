import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        String s = String.valueOf(n);
        String[] ss = s.split("");
        
        for(int i=0;i<ss.length;i++){
            answer += Integer.parseInt(ss[i]);
        }

        return answer;
    }
}