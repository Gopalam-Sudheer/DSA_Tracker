class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind=0
        end=0
        n=len(nums)
        while end<n:
            if nums[ind]!=nums[end]:
                ind+=1
                nums[ind],nums[end]=nums[end],nums[ind]
            end+=1
        return ind+1