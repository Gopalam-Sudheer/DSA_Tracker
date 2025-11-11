class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(nums,k):
            d={}
            start=0
            end=0
            n=len(nums)
            ans=0
            while end<n:
                d[nums[end]]=d.get(nums[end],0)+1
                while len(d)>k:
                    d[nums[start]]-=1
                    if d[nums[start]]==0:
                        del d[nums[start]]
                    start+=1
                ans+=end-start+1
                end+=1
            return ans
        return helper(nums,k)-helper(nums,k-1)