import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int max_w = 0, max_h = 0;

        for (int[] size : sizes) {
            int width = Math.max(size[0], size[1]);
            int height = Math.min(size[0], size[1]);

            max_w = Math.max(max_w, width);
            max_h = Math.max(max_h, height);
        }

        return max_w * max_h;
    }
}