class Solution {
    public int helper(int[][] dp,int[] coins, int ind, int amount){
        if(amount==0){
            return 1;
        }
        if(ind<0){
            return 0;
        }
        if (dp[ind][amount]!=-1){
            return dp[ind][amount];
        }
        int ans=helper(dp,coins,ind-1,amount);
        if(coins[ind]<=amount){
            ans=ans+helper(dp,coins,ind,amount-coins[ind]);
        }
        dp[ind][amount]=ans;
        return dp[ind][amount];
    }
  
    public int change(int amount, int[] coins) {
        int[][] dp=new int[coins.length][amount+1];
        for(int i=0;i<coins.length;i++){
            for(int j=0;j<amount+1;j++){
                dp[i][j]=-1;
            }
        }
        return helper(dp,coins,coins.length-1,amount);
    }
}