class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans=0
        total=0
        s=0
        for i in range(len(gas)):
            total+=gas[i]-cost[i]
            s+=gas[i]-cost[i]
            if s<0:
                s=0
                ans=i+1
        if total<0:
            return -1
        else:
            return ans