class Solution:
    def isHappy(self, n: int) -> bool:
        def fun(num):
            val=0
            while num>0:
                temp=num%10
                val+=temp**2
                num//=10
            return val
        if n==1:
            return True
        first=n
        sec=fun(first)
        while first!=sec:
            first=fun(first)
            sec=fun(fun(sec))
            if first==1 or sec==1:
                return True
        return False


        