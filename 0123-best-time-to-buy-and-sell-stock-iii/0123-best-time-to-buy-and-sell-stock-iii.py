class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def helper(dp,arr,ind,buy,k):
            if k==0:
                return 0
            if ind==len(arr):
                return 0
            if dp[ind][buy][k]!=-1:
                return dp[ind][buy][k]
            if buy:
                profit=max(helper(dp,arr,ind+1,1,k),-1*arr[ind]+helper(dp,arr,ind+1,0,k))
            else:
                profit=max(arr[ind]+helper(dp,arr,ind+1,1,k-1),helper(dp,arr,ind+1,0,k))
            dp[ind][buy][k]=profit
            return dp[ind][buy][k]
        dp=[[[-1 for _ in range(3)] for _ in range(2)] for _ in range(len(prices))]
        return helper(dp,prices,0,1,2)