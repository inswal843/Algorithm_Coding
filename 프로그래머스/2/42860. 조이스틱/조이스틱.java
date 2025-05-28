class Solution {
    /**
     * 풀이
     * 
     * 1. 각 문자를 A에서 목표 문자로 변경하는 최소 조작 횟수 계산 (상하 이동)
     * 2. 커서를 이동하는 최소 횟수 계산 (좌우 이동)
     *    - 오른쪽으로만 이동
     *    - 왼쪽으로만 이동
     *    - 오른쪽으로 갔다가 왼쪽으로 되돌아가기
     *    - 왼쪽으로 갔다가 오른쪽으로 되돌아가기
     * 3. 연속된 A 구간을 고려하여 최적의 이동 경로 선택
     * 
     * 시간 복잡도:
     * 문자열 길이 n에 대해 각 위치에서 최적 경로를 계산하므로
     * O(n^2)
     */
    public int solution(String name) {
        int answer = 0;
        int len = name.length();
        
        // 1. 각 문자를 변경하는데 필요한 상하 조작 횟수 계산
        for (int i = 0; i < len; i++) {
            char target = name.charAt(i);
            // A에서 target으로 가는 최소 거리 (위로 가거나 아래로 가거나)
            int up = target - 'A';
            int down = 'Z' - target + 1;
            answer += Math.min(up, down);
        }
        
        // 2. 좌우 이동 최소 횟수 계산
        int minMove = len - 1; // 기본값: 오른쪽으로만 쭉 이동
        
        for (int i = 0; i < len; i++) {
            // i 다음부터 연속된 A의 마지막 인덱스 찾기
            int nextIdx = i + 1;
            while (nextIdx < len && name.charAt(nextIdx) == 'A') {
                nextIdx++;
            }
            
            // 네 가지 이동 방법 중 최소값 선택
            // 1) 오른쪽으로만 이동
            // 2) 왼쪽으로만 이동
            // 3) 오른쪽으로 i까지 갔다가 처음으로 돌아와서 왼쪽으로 이동
            // 4) 왼쪽으로 갔다가 오른쪽으로 i까지 이동
            
            // i까지 갔다가 돌아오는 거리 + 뒤에서부터 nextIdx까지의 거리
            int moveRight = 2 * i + len - nextIdx;
            // 뒤에서부터 nextIdx까지 갔다가 돌아오는 거리 + i까지의 거리
            int moveLeft = i + 2 * (len - nextIdx);
            
            minMove = Math.min(minMove, Math.min(moveRight, moveLeft));
        }
        
        answer += minMove;
        return answer;
    }
}