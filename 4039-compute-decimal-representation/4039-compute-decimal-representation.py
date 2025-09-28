class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans=[]
        po=1
        while n>0:
            rem=n%10
            if rem!=0:
                ans=[po*rem]+ans
            po*=10
            n//=10
        return ans