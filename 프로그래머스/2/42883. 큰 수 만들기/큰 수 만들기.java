import java.util.*;

class Solution {
    /**
     * 풀이
     * 
     * Stack을 활용한 그리디 알고리즘으로 해결
     * 1. 스택에 숫자를 하나씩 넣으면서 다음 규칙 적용:
     *    - 스택의 top이 현재 숫자보다 작고, 아직 제거할 수 있으면 pop
     *    - 현재 숫자를 스택에 push
     * 2. k개를 모두 제거하지 못했다면 뒤에서부터 제거
     * 3. 스택에 남은 숫자들이 최대값을 형성
     * 
     * 시간 복잡도:
     * 각 숫자는 최대 한 번 push되고 한 번 pop되므로
     * O(n) where n = number.length()
     */
    public String solution(String number, int k) {
        Stack<Character> stack = new Stack<>();
        int toRemove = k;
        
        for (int i = 0; i < number.length(); i++) {
            char current = number.charAt(i);
            
            // 스택이 비어있지 않고, 제거할 개수가 남아있고,
            // 스택의 top이 현재 숫자보다 작으면 제거
            while (!stack.isEmpty() && toRemove > 0 && stack.peek() < current) {
                stack.pop();
                toRemove--;
            }
            
            stack.push(current);
        }
        
        // 아직 제거할 개수가 남아있다면 뒤에서부터 제거
        while (toRemove > 0) {
            stack.pop();
            toRemove--;
        }
        
        // 스택의 내용을 문자열로 변환
        StringBuilder answer = new StringBuilder();
        for (char c : stack) {
            answer.append(c);
        }
        
        return answer.toString();
    }
}