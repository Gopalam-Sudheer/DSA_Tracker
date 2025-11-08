class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return n
        pre=[1]*n
        suff=[1]*n
        for i in range(1,n):
            if nums[i-1]<=nums[i]:
                pre[i]=1+pre[i-1]
        for i in range(n-2,-1,-1):
            if nums[i]<=nums[i+1]:
                suff[i]=1+suff[i+1]
        ans=max(pre)
        for i in range(n):
            c=1
            if i==0:
                c=1+suff[1]
            elif i==n-1:
                c=1+pre[i-1]
            else:
                if nums[i+1]>=nums[i-1]:
                    c=1+pre[i-1]+suff[i+1]
                else:
                    c=max(1+pre[i-1],1+suff[i+1],ans)
            ans=max(ans,c)
        return min(ans,n)