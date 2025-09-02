class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def helper(dp,s1,s2,i,j):
            if i==len(s1) and j<len(s2):
                return len(s2)-j
            if i<len(s1) and j==len(s2):
                return len(s1)-i
            if i==len(s1) and j==len(s2):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if s1[i]==s2[j]:
                ans=helper(dp,s1,s2,i+1,j+1)
            else:
                a=1+helper(dp,s1,s2,i+1,j)
                b=1+helper(dp,s1,s2,i,j+1)
                c=1+helper(dp,s1,s2,i+1,j+1)
                ans=min(a,b,c)
            dp[i][j]=ans
            return dp[i][j]
        dp=[[-1 for i in range(len(word2))] for j in range(len(word1))]
        return helper(dp,word1,word2,0,0)
                                                                                                                                                                                                                                                                                             