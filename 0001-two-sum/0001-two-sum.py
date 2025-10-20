class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        eleIndex=[]
        for i in range(n):
            eleIndex.append([nums[i],i])
        left,right=0,n-1
        eleIndex.sort(key=lambda x:x[0])
        while left<right:
            sum_val=eleIndex[left][0]+eleIndex[right][0]
            if sum_val==target:
                return [eleIndex[left][1],eleIndex[right][1]]
            elif sum_val<target:
                left+=1
            else:
                right-=1
        return [-1,-1]