class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum=[]
        cur=0
        for i in nums:
            cur+=i
            self.preSum.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        r=self.preSum[right]
        l=self.preSum[left-1] if left-1>=0 else 0 
        return r-l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)