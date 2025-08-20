class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def lower_bound(temp,target):
            left=0
            right=len(temp)-1
            while left<=right:
                mid=(left+right)//2
                if temp[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return left
        n=len(nums)
        temp=[]
        temp.append(nums[0])
        for i in range(1,n):
            if nums[i]>temp[-1]:
                temp.append(nums[i])
            else:
                ind=lower_bound(temp,nums[i])
                temp[ind]=nums[i]
        return len(temp)
            