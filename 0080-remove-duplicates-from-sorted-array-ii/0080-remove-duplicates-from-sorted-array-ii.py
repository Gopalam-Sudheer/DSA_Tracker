class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        while j<len(nums):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
            else:
                if i-1>=0 and nums[i]==nums[i-1]:
                    pass
                else:
                    i+=1
                    nums[i]=nums[j]
            j+=1
        return i+1