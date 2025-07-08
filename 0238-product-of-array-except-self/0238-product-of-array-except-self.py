class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        prod=1
        for i in nums:
            ans.append(prod)
            prod*=i
        prod=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=prod
            prod*=nums[i]
        return ans