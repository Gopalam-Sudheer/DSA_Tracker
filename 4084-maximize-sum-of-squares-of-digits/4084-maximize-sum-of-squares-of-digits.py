class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num*9<sum:
            return ""
        nines=sum//9
        rem=""
        zeroes=num-nines
        if nines<num:
            rem=sum%9
            zeroes-=1
        return '9'*nines+str(rem)+'0'*zeroes
