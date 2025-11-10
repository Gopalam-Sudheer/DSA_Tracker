class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d={}
        s=0
        ans=0
        for i in range(len(nums)):
            s+=nums[i]
            if s==goal:
                ans+=1
            ans+=d.get(s-goal,0)
            d[s]=d.get(s,0)+1
        return ans