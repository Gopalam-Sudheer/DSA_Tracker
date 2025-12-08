class Solution:
    def countTriples(self, n: int) -> int:
        ans=0
        for i in range(3,n+1):
            start=1
            end=i-1
            while start<end:
                square=start**2+end**2
                if square>i**2:
                    end-=1
                elif square<i**2:
                    start+=1
                else:
                    ans+=2
                    start+=1
                    end-=1
        return ans
