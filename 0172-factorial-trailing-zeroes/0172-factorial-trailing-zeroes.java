class Solution {
    public int trailingZeroes(int n) {
        int ans=0;
        int temp=n;
        while(temp>=5){
            ans+=temp/5;
            temp/=5;
        }
        return ans;
    }
}