class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        def f(dp,i,j,cuts):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            mini=float('inf')
            for ind in range(i,j+1):
                cost=cuts[j+1]-cuts[i-1]+f(dp,i,ind-1,cuts)+f(dp,ind+1,j,cuts)
                mini=min(mini,cost)
            dp[i][j]=mini
            return dp[i][j]
        cuts=[0]+cuts+[n]
        cuts.sort()
        dp=[[-1 for i in range(len(cuts))] for j in range(len(cuts))]
        return f(dp,1,len(cuts)-2,cuts)