class Solution:
    def smallestNumber(self, n: int) -> int:
        a=math.log(n,2)
        return 2**(math.floor(a)+1)-1