class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ones=0
        start,end=0,0
        ans=0
        while end<len(nums):
            ones+=nums[end]
            if end-start+1-ones<=k:
                ans=max(ans,end-start+1)
            else:
                ones-=nums[start]
                start+=1
            end+=1
        return ans