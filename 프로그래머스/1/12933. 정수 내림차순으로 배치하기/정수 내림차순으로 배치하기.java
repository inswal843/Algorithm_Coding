import java.util.*;
class Solution {
    public long solution(long n) {
        String s = String.valueOf(n);
        String[] ss = s.split("");
        // String 배열을 Integer 배열로 변환
        Integer[] nn = Arrays.stream(ss).map(Integer::parseInt).toArray(Integer[]::new);
        // 내림차순 정렬
        Arrays.sort(nn, Collections.reverseOrder());
        // Integer 배열을 int 배열로 변환
        int[] result = Arrays.stream(nn).mapToInt(Integer::intValue).toArray();
        StringBuilder result2 = new StringBuilder();
        for(int i = 0; i<result.length; i++){
            result2.append(result[i]);
        }
        long answer = Long.parseLong(result2.toString());
        return answer;
    }
}