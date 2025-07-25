class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans=max(nums)
        res=0
        s=set()
        for i in nums:
            if i>=0 and i not in s:
                res+=i
            s.add(i)
        if ans<0:
            return ans
        else:
            return res