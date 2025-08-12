class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        d={}
        def helper(cur_sum,ind):
            if (cur_sum,ind) in d:
                return d[(cur_sum,ind)]
            if ind==len(nums):
                if cur_sum==target:
                    return 1
                return 0
            d[(cur_sum,ind)]=helper(cur_sum+nums[ind],ind+1)+helper(cur_sum-nums[ind],ind+1)
            return d[(cur_sum,ind)]
        return helper(0,0)