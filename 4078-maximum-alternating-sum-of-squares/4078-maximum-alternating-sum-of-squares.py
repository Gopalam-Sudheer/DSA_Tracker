class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: abs(x))
        start=0
        end=len(nums)-1
        ans=0
        while start<end:
            ans+=(nums[end])**2
            ans-=(nums[start])**2
            print()
            start+=1
            end-=1
        if start==end:
            ans+=(nums[start])**2
        return ans