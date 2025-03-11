import java.util.*;

class Solution {
    public int solution(String numbers) {
        List<String> nums = Arrays.asList(numbers.split(""));
        Set<Integer> primeSet = new HashSet<>();

        for (int length = 1; length <= nums.size(); length++) {
            backTrack(primeSet, new boolean[nums.size()], nums, length, 0, "");
        }
        return primeSet.size();
    }

    public void backTrack(Set<Integer> primeSet, boolean[] visited, List<String> nums, int limit, int curLength, String curNumber) {
        if (curLength == limit){
            int number = Integer.parseInt(curNumber);
            if(isPrime(number)){
                primeSet.add(number);
            }
        } else {
            for (int i = 0; i < nums.size(); i++) {
                if (!visited[i]){
                    visited[i] = true;
                    backTrack(primeSet, visited, nums, limit, curLength+1, curNumber + nums.get(i));
                    visited[i] = false;
                }
            }
        }
    }

    public boolean isPrime(int number) {
        if(number < 2) return false;
        for (int i = 2; i <= (int) Math.sqrt(number); i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
}