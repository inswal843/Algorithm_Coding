import java.util.*;

class Solution {
    public class Node {
        public String curStr;
        public int curStep;
        
        public Node(String str, int step){
            curStr = str;
            curStep = step;
        }
    }
    
    public int solution(String begin, String target, String[] words) {
        int n = begin.length();
        
        boolean[] visited = new boolean[words.length];
        Queue<Node> queue = new LinkedList<>();
        
        queue.offer(new Node(begin, 0));
        
        while(!queue.isEmpty()){
            Node curNode = queue.poll();
            
            if(curNode.curStr.equals(target)) return curNode.curStep;
            
            for(int i=0; i < words.length; i++){
                if(!visited[i]){
                    int missMatched = 0;
                
                    for(int j = 0; j < n; j++){
                        if(curNode.curStr.charAt(j)!=words[i].charAt(j)){
                            missMatched++;
                            if(missMatched > 1) break;
                        }
                    }
                    if(missMatched == 1){
                        visited[i] = true;
                        queue.offer(new Node(words[i], curNode.curStep+1));
                    }
                }

            }
        }
        return 0;
    }
}