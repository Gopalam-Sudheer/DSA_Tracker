class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):
            if n<=0:
                return 1
            half=pow(x,n//2)
            if n%2==0:
                return half*half
            else:
                return x*half*half
        sign=n>0
        x=pow(x,abs(n))
        if sign:
            return x
        else:
            return 1/x

