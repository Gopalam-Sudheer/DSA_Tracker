class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def helper(dp,s1,s2,i,j):
            if i==len(s1) and j==len(s2):
                return True
            if i==len(s1) and j<len(s2):
                while j<len(s2) and s2[j]=='*':
                    j+=1
                return j==len(s2)
            if i<len(s1) and j==len(s2):
                return False
            if dp[i][j]!=None:
                return dp[i][j]
            ans=False
            if s1[i]==s2[j] or s2[j]=='?':
                ans=helper(dp,s1,s2,i+1,j+1)
            elif s2[j]=='*':
                a=helper(dp,s1,s2,i+1,j)
                b=helper(dp,s1,s2,i+1,j+1)
                c=helper(dp,s1,s2,i,j+1)
                ans=(a or b or c)
            dp[i][j]=ans
            return dp[i][j]
        dp=[[None for i in range(len(p))] for j in range(len(s))]
        return helper(dp,s,p,0,0)
                                                                                                                                                                                                                                                                                                                                                