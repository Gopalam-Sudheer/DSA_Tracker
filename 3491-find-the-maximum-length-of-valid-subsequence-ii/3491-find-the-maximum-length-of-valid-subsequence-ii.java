class Solution {
    public int maximumLength(int[] nums, int k) {
        int[][] dp=new int[k][k];
        int ans=0;
        for(int i=0;i<nums.length;i++){
            nums[i]%=k;
            for(int prev=0;prev<k;prev++){
                dp[prev][nums[i]]=dp[nums[i]][prev]+1;
                ans=Math.max(ans,dp[prev][nums[i]]);
            }
        }
        return ans;
    }
}