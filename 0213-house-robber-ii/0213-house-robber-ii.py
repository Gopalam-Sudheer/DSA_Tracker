class Solution:
    def helper(self,money):
        l=[0]*len(money)
        l[0]=money[0]
        for i in range(1,len(money)):
            pick=money[i]
            if i-2>=0:
                pick+=l[i-2]
            notpick=l[i-1]
            l[i]=max(pick,notpick)
        return l[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        ans1=self.helper(nums[:-1])
        ans2=self.helper(nums[1:])
        return max(ans1,ans2)
        