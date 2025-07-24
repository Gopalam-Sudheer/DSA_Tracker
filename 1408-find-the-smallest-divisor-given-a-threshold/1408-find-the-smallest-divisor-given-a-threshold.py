class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        limit=threshold
        def helper(nums,k):
            res=0
            for i in nums:
                res+=math.ceil(i/k)
            return res
        low=1
        high=max(nums)
        while low<=high:
            mid=(low+high)//2
            t=helper(nums,mid)
            if t>limit:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans