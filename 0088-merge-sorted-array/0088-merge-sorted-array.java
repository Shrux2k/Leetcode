class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) 
    {
        int []temp = new int[m+n];
        int i;
        for(i=0; i<m;i++)
            temp[i] = nums1[i];
        for(int j =0;j<n;j++)
            temp[i+j] = nums2[j];
        for(int x =0;x<m+n;x++)
            nums1[x] = temp[x];
        Arrays.sort(nums1);
    }
}