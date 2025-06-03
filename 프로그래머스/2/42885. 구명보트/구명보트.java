import java.util.*;

class Solution {
    /**
     * 풀이
     * 
     * 투 포인터를 활용한 그리디 알고리즘으로 해결
     * 1. 사람들의 몸무게를 오름차순으로 정렬
     * 2. 가장 가벼운 사람과 가장 무거운 사람을 짝지어 태우기 시도
     *    - 두 사람의 합이 limit 이하면 함께 태움
     *    - limit 초과면 무거운 사람만 태움
     * 3. 모든 사람을 태울 때까지 반복
     * 
     * 시간 복잡도:
     * 정렬 O(n log n) + 투 포인터 탐색 O(n)
     * O(n log n) where n = people.length
     */
    public int solution(int[] people, int limit) {
        // 몸무게 오름차순 정렬
        Arrays.sort(people);
        
        int boats = 0;
        int left = 0;  // 가장 가벼운 사람을 가리키는 포인터
        int right = people.length - 1;  // 가장 무거운 사람을 가리키는 포인터
        
        while (left <= right) {
            // 가장 가벼운 사람과 가장 무거운 사람의 합이 limit 이하인 경우
            if (people[left] + people[right] <= limit) {
                left++;  // 가벼운 사람도 태움
                right--; // 무거운 사람도 태움
            }
            // limit을 초과하는 경우
            else {
                right--; // 무거운 사람만 태움
            }
            
            boats++; // 보트 하나 사용
        }
        
        return boats;
    }
}