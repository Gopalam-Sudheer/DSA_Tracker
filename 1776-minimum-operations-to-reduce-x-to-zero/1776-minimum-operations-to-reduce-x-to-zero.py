class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        low=0
        high=0
        ans=0
        s=sum(nums)-x
        if s==0:
            return len(nums)
        while high<len(nums):
            s-=nums[high]
            while s<0 and low<high:
                s+=nums[low]
                low+=1
            if s==0:
                ans=max(ans,high-low+1)
            high+=1
        return -1 if ans==0 else len(nums)-ans
