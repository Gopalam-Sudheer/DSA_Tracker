class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n=len(capacity)
        res=0
        pre=0
        d=defaultdict(lambda: defaultdict(int))
        for i in range(n):
            res+=d[capacity[i]].get(pre-capacity[i],0)
            pre+=capacity[i]
            d[capacity[i]][pre]+=1
            if i>0 and capacity[i]==0 and capacity[i-1]==0:
                res-=1
        return res