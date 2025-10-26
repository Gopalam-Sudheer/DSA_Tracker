class Solution {
    private long reverse(long val){
        long ans=0;
        while(val>0){
            long rem=val%10;
            if(rem!=0){
                ans=ans*10+rem;
            }
            val/=10;
        }
        return ans;
    }
    public long removeZeros(long n) {
        return reverse(reverse(n));
    }
}