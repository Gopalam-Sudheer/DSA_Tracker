class Solution:
    def genPerm(self,ans,nums,ind):
        if ind==len(nums):
            ans.append(nums[:])
            return
        for i in range(ind,len(nums)):
            nums[ind],nums[i]=nums[i],nums[ind]
            self.genPerm(ans,nums,ind+1)
            nums[ind],nums[i]=nums[i],nums[ind]


    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        self.genPerm(ans,nums,0)
        return ans