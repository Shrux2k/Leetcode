class Solution {
    public int pivotIndex(int[] nums) 
    {
        int l = nums.length;
        int []left = new int[l];
        int []right = new int[l];
        left[0] = nums[0];
        right[l-1] = nums[l-1];
        
        for(int i =1;i<l;i++)
        {
            left[i] = nums[i]+left[i-1];
            right[l-1-i] = nums[l-1-i] + right[l-i];
        }
        
        for(int i =0;i<l;i++)
        {
            if(left[i]==right[i])
            {
                return i;
            }
        }
        
        return -1;
        
    }
}