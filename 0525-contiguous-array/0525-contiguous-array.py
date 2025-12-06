class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={}
        c=0
        ans=0
        for i in range(len(nums)):
            if nums[i]==0:
                c-=1
            else:
                c+=1
            if c==0:
                ans=i+1
            if c in d:
                ans=max(ans,i-d[c])
            if c not in d:
                d[c]=i
        return ans