class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        nums=bloomDay
        def helper(nums,k,w):
            ans=0
            cur=0
            for i in nums:
                if i<=k:
                    cur+=1
                else:
                    cur=0
                if cur==w:
                    ans+=1
                    cur=0
            return ans
        ans=-1
        if m*k>len(nums):
            return ans
        low=min(nums)
        high=max(nums)
        while low<=high:
            mid=(low+high)//2
            t=helper(nums,mid,k)
            if t>=m:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans