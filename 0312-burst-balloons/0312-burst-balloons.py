class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def f(dp,i,j,arr):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            maxi=float('-inf')
            for ind in range(i,j+1):
                coins=arr[i-1]*arr[ind]*arr[j+1]+f(dp,i,ind-1,arr)+f(dp,ind+1,j,arr)
                if maxi<coins:
                    maxi=coins
            dp[i][j]=maxi
            return dp[i][j]
        n=len(nums)
        nums=[1]+nums+[1]
        dp=[[-1 for i in range(n+1)] for j in range(n+1)]
        return f(dp,1,n,nums)
                                                                                                                                                                                                                                    
        