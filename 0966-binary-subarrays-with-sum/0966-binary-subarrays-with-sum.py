class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d={}
        ans=0
        d[0]=1
        for i in range(len(nums)):
            if i>0:
                nums[i]+=nums[i-1]
            if nums[i]-goal in d:
                ans+=d[nums[i]-goal]
            d[nums[i]]=d.get(nums[i],0)+1
        return ans