class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(nums,goal):
            if goal<0:
                return 0
            start=0
            end=0
            ans=0
            n=len(nums)
            window=0
            while end<n:
                window+=nums[end]
                while start<=end and window>goal:
                    window-=nums[start]
                    start+=1
                ans+=end-start+1
                end+=1
            return ans
        return helper(nums,goal)-helper(nums,goal-1)