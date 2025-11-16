class Solution:
    def numSub(self, s: str) -> int:
        ans,ones=0,0
        for i in s:
            if i=='1':
                ones+=1
            else:
                ones=0
            ans+=ones
            ans%=1000000007
        return ans