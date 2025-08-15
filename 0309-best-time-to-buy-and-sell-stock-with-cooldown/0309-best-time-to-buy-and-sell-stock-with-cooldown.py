class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def helper(dp,arr,ind,buy):
            if ind>=len(arr):
                return 0
            if dp[buy][ind]!=-1:
                return dp[buy][ind]
            if buy==1:
                profit=max(-1*arr[ind]+helper(dp,arr,ind+1,0),helper(dp,arr,ind+1,1))
            else:
                profit=max(arr[ind]+helper(dp,arr,ind+2,1),helper(dp,arr,ind+1,0))
            dp[buy][ind]=profit
            return dp[buy][ind]
        dp=[[-1 for _ in range(len(prices))] for _ in range(2)]
        return helper(dp,prices,0,1)