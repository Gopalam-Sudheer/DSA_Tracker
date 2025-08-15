class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def helper(dp,arr,ind,buy,fee):
            if ind==len(arr):
                return 0
            if dp[buy][ind]!=-1:
                return dp[buy][ind]
            if buy==1:
                profit=max(-1*arr[ind]+helper(dp,arr,ind+1,0,fee),helper(dp,arr,ind+1,1,fee))
            else:
                profit=max(arr[ind]+helper(dp,arr,ind+1,1,fee)-fee,helper(dp,arr,ind+1,0,fee))
            dp[buy][ind]=profit
            return dp[buy][ind]
        dp=[[-1 for _ in range(len(prices))] for _ in range(2)]
        return helper(dp,prices,0,1,fee)