class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start=0
        ones=0
        ans=0
        n=len(nums)
        for end in range(n):
            if nums[end]==1:
                ones+=1
            if (end-start+1-ones)<=k:
                ans=max(ans,end-start+1)
            else:
                if nums[start]==1:
                    ones-=1
                start+=1
        return ans