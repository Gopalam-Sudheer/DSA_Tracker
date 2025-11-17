class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ind=0
        for i in range(len(nums)):
            if nums[i]==1:
                ind=i
                break
        prev=ind
        ind+=1
        while ind<len(nums):
            if nums[ind]==1:
                if ind-prev<=k:
                    return False
                prev=ind
            ind+=1
        return True