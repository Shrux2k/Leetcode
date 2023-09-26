class Solution {
    public int fib(int n) 
    {
        if(n==1 || n==0)
        {
            return n;
        }
    
    
    int fn1 = fib(n-1);
    int fn2 = fib(n-2);
    int nth = fn1+fn2;
    return nth;
    }
}