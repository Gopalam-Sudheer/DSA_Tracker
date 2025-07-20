class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ones=0
        start=0
        end=0
        ans=0
        while end<len(nums):
            if nums[end]==1:
                ones+=1
            if end-start+1-ones<=k:
                ans=max(ans,end-start+1)
            else:
                if nums[start]==1:
                    ones-=1
                start+=1
            end+=1
        return ans