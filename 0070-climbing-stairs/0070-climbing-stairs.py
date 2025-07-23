class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        f=2
        s=1
        for i in range(3,n+1):
            z=f+s
            s=f
            f=z
        return f