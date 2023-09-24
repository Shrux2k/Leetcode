import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap <Integer, Integer> twoSum = new HashMap<Integer, Integer>();

        int x = 0;

        for(int i =0;i<nums.length;i++)
        {
            x = target - nums[i];
            if(twoSum.containsKey(x))
            {
                return new int[] {twoSum.get(x),i};
            }
            else
            {
                twoSum.put(nums[i],i);
            }

        }  
        return new int[] {};      
    }
    
}