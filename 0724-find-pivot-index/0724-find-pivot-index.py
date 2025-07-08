class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        cur=0
        for i in range(len(nums)):
            s-=nums[i]
            if cur==s:
                return i
            cur+=nums[i]
        return -1