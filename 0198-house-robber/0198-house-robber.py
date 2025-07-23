class Solution:
    def rob(self, nums: List[int]) -> int:
        l=nums[:]
        l[0]=nums[0]
        for i in range(1,len(nums)):
            ma=nums[i]
            if i-2>=0:
                ma+=l[i-2]
            ma=max(l[i-1],ma)
            l[i]=ma
        return l[-1]