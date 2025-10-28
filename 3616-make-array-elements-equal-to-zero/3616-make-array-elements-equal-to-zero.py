class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        pre_sum=[]
        suff_sum=[]
        pre=0
        suf=0
        for i in range(len(nums)):
            pre_sum.append(pre)
            suff_sum.append(suf)
            pre+=nums[i]
            suf+=nums[len(nums)-1-i]
        suff_sum=suff_sum[::-1]
        ans=0
        for i in range(len(nums)):
            if nums[i]==0:
                if pre_sum[i]==suff_sum[i]:
                    ans+=2
                elif abs(pre_sum[i]-suff_sum[i])==1:
                    ans+=1
        return ans