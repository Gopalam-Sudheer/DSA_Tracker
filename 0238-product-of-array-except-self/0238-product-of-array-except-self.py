class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes=0
        prod=1
        ans=[0 for j in range(len(nums))]
        for i in nums:
            if i==0:
                zeroes+=1
            else:
                prod*=i
        if zeroes>1:
            return ans
        for ind in range(len(nums)):
            if zeroes==0:
                ans[ind]=prod//nums[ind]
            elif nums[ind]==0:
                ans[ind]=prod
        return ans