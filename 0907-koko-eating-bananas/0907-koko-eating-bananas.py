class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        nums=piles
        def helper(nums,val):
            s=0
            for i in nums:
                s+=math.ceil(i/val)
            return s
        low=1
        high=max(nums)
        while low<=high:
            mid=(low+high)//2
            hours=helper(nums,mid)
            if hours>h:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans