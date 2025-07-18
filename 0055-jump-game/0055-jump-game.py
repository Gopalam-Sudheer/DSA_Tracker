class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach=0
        for i in range(len(nums)-1):
            reach=max(reach,i+nums[i])
            if reach<=i:
                return False
        return True