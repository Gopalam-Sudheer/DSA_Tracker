class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num=start^goal
        ans=0
        while num>0:
            ans+=1
            num=num&(num-1)
        return ans