class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                fast=0
                break
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow
        
            
        

