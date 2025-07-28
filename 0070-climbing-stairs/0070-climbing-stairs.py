class Solution:
    def climbStairs(self, n: int) -> int:
        prev1=2
        prev2=1
        if n<=2:
            return n
        for i in range(3,n+1):
            cur=prev1+prev2
            prev2=prev1
            prev1=cur
        return prev1