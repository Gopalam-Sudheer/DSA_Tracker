class Solution {
    public int helper(int[][] dp,int[] prices,int buy,int index){
        if(index==prices.length){
            return 0;
        }
        if(dp[buy][index]!=-1){
            return dp[buy][index]; 
        }
        int profit=0;
        if(buy==0){
            profit=Math.max(-1*prices[index]+helper(dp,prices,1,index+1),helper(dp,prices,0,index+1));
        }else{
            profit=Math.max(prices[index]+helper(dp,prices,0,index+1),helper(dp,prices,1,index+1));
        }
        dp[buy][index]=profit;
        return dp[buy][index];
    }
    public int maxProfit(int[] prices) {
        int[][] dp=new int[2][prices.length];
        for(int[] row : dp){
            Arrays.fill(row,-1);
        }
        return helper(dp,prices,0,0);
    }
}