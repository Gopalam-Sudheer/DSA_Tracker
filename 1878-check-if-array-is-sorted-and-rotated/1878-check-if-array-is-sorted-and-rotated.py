class Solution:
    def check(self, nums: List[int]) -> bool:
        c=0
        l=len(nums)
        for i in range(l):
            if nums[i]>nums[(i+1)%l]:
                c+=1
        return c<=1