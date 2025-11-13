class Solution:
    def maxOperations(self, s: str) -> int:
        ind=0
        ans=0
        n=len(s)
        ones=0
        while ind<n:
            if s[ind]=='1':
                ones+=1
            else:
                while ind<n and s[ind]=='0':
                    ind+=1
                ans+=ones
                continue
            ind+=1
        return ans