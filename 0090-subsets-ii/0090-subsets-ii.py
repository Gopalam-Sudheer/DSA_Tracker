class Solution:
    def generateSets(self,ans,nums,ind,temp):
        if ind==len(nums):
            ans.append(temp[:])
            return
        temp.append(nums[ind])
        self.generateSets(ans,nums,ind+1,temp)
        temp.pop()
        while ind+1<len(nums) and nums[ind]==nums[ind+1]:
            ind+=1
        self.generateSets(ans,nums,ind+1,temp)



    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        self.generateSets(ans,nums,0,[])
        return ans