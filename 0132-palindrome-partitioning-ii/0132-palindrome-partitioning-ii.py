class Solution:
    def minCut(self, s: str) -> int:
        def f(dp,i,j,s):
            if i==len(s):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            ans=float('inf')
            for ind in range(i,j+1):
                k=s[i:ind+1]
                if k==k[::-1]:
                    ans=min(1+f(dp,ind+1,j,s),ans)
            dp[i][j]=ans
            return dp[i][j]
        dp=[[-1 for i in range(len(s))] for j in range(len(s))]
        return f(dp,0,len(s)-1,s)-1