class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end=0
        n=len(nums)
        start=0
        while end<n:
            if nums[end]!=val:
                nums[start]=nums[end]
                start+=1
            end+=1
        return start