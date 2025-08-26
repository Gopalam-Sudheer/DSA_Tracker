class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def helper(dp,ind,arr,target):
            if target<0 or ind<0:
                return False
            if target==0:
                return True
            if dp[ind][target]!=None:
                return dp[ind][target]
            dp[ind][target]=helper(dp,ind-1,arr,target-arr[ind]) or helper(dp,ind-1,arr,target)
            return dp[ind][target] 
        s=sum(nums)
        if s%2==1:
            return False
        target=s//2
        dp=[[None for i in range(target+1)] for j in range(len(nums))]
        return helper(dp,len(nums)-1,nums,target)