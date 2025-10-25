class Solution:
    def totalMoney(self, n: int) -> int:
        ans=0
        s=0
        for i in range(1,n+1):
            val1=i%7
            if val1==0:
                ans+=7
            else:
                ans+=val1
            ans+=s
            if i%7==0:
                s+=1
        return ans