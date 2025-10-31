class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        if len(nums)==2:
            return nums
        ans=[]
        xor=0
        xor1=0
        for i in range(len(nums)):
            xor^=nums[i]
            if i<=len(nums)-3:
                xor1^=i
        total=xor^xor1
        diff=total&(total-1)
        c=total^diff
        ans1=0
        ans2=0
        for i in range(len(nums)):
            if c&nums[i]==0:
                ans1^=nums[i]
            else:
                ans2^=nums[i]
            if i<=len(nums)-3:
                if c&i==0:
                    ans1^=i
                else:
                    ans2^=i
        return [min(ans1,ans2),max(ans1,ans2)]