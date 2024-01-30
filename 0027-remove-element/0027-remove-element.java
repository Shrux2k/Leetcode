class Solution {
   public int removeElement(int[] nums, int val) {
        int frqCount = 0;

        for (int i = 0; i < nums.length; i++) {
            nums[i - frqCount] = nums[i];
            if (nums[i] == val) {
                frqCount++;
            }
        }

        return nums.length - frqCount;
    }
}