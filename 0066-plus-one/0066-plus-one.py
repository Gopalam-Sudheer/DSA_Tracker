class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem=1
        for i in range(len(digits)-1,-1,-1):
            temp=digits[i]+rem
            digits[i]=temp%10
            rem=temp//10
            if rem==0:
                return digits
        return [1]+digits
        