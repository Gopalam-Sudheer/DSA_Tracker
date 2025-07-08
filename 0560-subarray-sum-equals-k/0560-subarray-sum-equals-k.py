class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumTrack={}
        preSum=0
        ans=0
        for i in nums:
            preSum+=i
            if preSum-k in sumTrack:
                ans+=sumTrack[preSum-k]
            if preSum==k:
                ans+=1
            sumTrack[preSum]=1+sumTrack.get(preSum,0)
        return ans