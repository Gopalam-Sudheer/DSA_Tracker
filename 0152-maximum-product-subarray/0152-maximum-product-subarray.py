class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod=1
        ans=nums[0]
        for i in range(len(nums)):
            prod*=nums[i]
            ans=max(ans,max(nums[i],prod))
            if prod==0:
                prod=1
        prod=1
        for i in range(len(nums)-1,-1,-1):
            prod*=nums[i]
            ans=max(ans,max(nums[i],prod))
            if prod==0:
                prod=1
        return ans
        

