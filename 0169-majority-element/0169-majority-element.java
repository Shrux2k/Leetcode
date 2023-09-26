class Solution {
    public int majorityElement(int[] nums) 
    {
        int i;
        int ret = 0;
       for(i =0;i<nums.length;i++)
       {
           int count = 0;
           for(int j =0; j<nums.length;j++)
           {
               if(nums[i] == nums[j])
               {
                   count++;
               }
           }
           ret = nums[i];
           int check = nums.length/2;
           if(count> check)
           {
               return nums[i];
           }
       }
        return ret;
    }
}