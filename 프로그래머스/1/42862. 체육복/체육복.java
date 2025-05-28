class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        // 1. 학생별 체육복 개수를 저장할 배열 생성 (인덱스 0은 사용하지 않음)
        int[] students = new int[n + 1];
        
        // 2. 모든 학생이 체육복 1개씩 가지고 있다고 초기화
        for (int i = 1; i <= n; i++) {
            students[i] = 1;
        }
        
        // 3. 도난당한 학생은 체육복 개수 -1
        for (int l : lost) {
            students[l]--;
        }
        
        // 4. 여벌 체육복을 가진 학생은 체육복 개수 +1
        for (int r : reserve) {
            students[r]++;
        }
        
        // 5. 체육복 빌려주기 처리
        for (int i = 1; i <= n; i++) {
            // 체육복이 없는 학생을 찾으면
            if (students[i] == 0) {
                // 앞 번호 학생이 여벌이 있으면 빌림
                if (i > 1 && students[i - 1] == 2) {
                    students[i - 1]--;
                    students[i]++;
                }
                // 뒷 번호 학생이 여벌이 있으면 빌림
                else if (i < n && students[i + 1] == 2) {
                    students[i + 1]--;
                    students[i]++;
                }
            }
        }
        
        // 6. 체육복을 가진 학생 수 계산
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            if (students[i] >= 1) {
                answer++;
            }
        }
        
        return answer;
    }
}