import java.util.*;

class Solution {
    public int solution(String numbers) {
        List<String> nums = Arrays.asList(numbers.split(""));

        Set<Integer> primeSet = new HashSet<>();


        for (int i = 1; i <= nums.size(); i++) {
            for (int j = 0; j < nums.size(); j++) {
                boolean[] visited = new boolean[nums.size()];
                visited[j] = true;
                backTrack(primeSet, visited, nums, i, 1, nums.get(j));
            }
        }

        int answer = primeSet.size();

        System.out.println("primeSet = " + primeSet);

        return answer;
    }

    public void backTrack(Set<Integer> set, boolean[] visited, List<String> nums, int limit, int index, String num) {
        if (index == limit){
            if(isPrime(num)){
                set.add(Integer.parseInt(num));
            }
        }else{
            for (int i = 0; i < nums.size(); i++) {
                if (visited[i] == false){
                    visited[i] = true;
                    backTrack(set, visited, nums, limit, index+1, num + nums.get(i));
                    visited[i] = false;
                }
            }
        }
    }

    public boolean isPrime(String numbers) {
        int number = Integer.parseInt(numbers);
        if(number < 2) return false;
        int sqrt = (int) Math.sqrt(number);
        for (int i = 2; i <= sqrt; i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
}