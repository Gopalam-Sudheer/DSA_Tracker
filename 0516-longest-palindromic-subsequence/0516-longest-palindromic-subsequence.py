class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def helper(dp,st,i,j):
            if i>j:
                return 0
            if i==j:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            if st[i]==st[j]:
                ans=2+helper(dp,st,i+1,j-1)
            else:
                ans=max(helper(dp,st,i+1,j),helper(dp,st,i,j-1))
            dp[i][j]=ans
            return dp[i][j]
        dp=[[-1 for i in range(len(s))] for j in range(len(s))]
        return helper(dp,s,0,len(s)-1)
        