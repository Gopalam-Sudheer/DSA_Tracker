class Solution {
    public int maxProfit(int[] prices) {
        int[][] dp=new int[2][prices.length+1];
        dp[0][prices.length]=0;
        dp[1][prices.length]=0;
        for(int index=prices.length-1;index>=0;index--){
            for(int buy=0;buy<=1;buy++){
                int profit=0;
                if(buy==0){
                    profit=Math.max(-1*prices[index]+dp[1][index+1],dp[0][index+1]);
                }
                if(buy==1){
                    profit=Math.max(dp[1][index+1],prices[index]+dp[0][index+1]);
                }
                dp[buy][index]=profit;
            }
        }
        return dp[0][0];
    }
}