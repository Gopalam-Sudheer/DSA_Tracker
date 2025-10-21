class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct=set()
        for i in nums:
            if i in distinct:
                return True
            distinct.add(i)
        return False