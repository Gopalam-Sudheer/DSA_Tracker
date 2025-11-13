class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort(key=lambda x: x[0])
        for i in intervals:
            if len(ans)==0:
                ans.append(i)
            elif ans[-1][1]<i[0]:
                ans.append(i)
            else:
                ans[-1][0]=min(ans[-1][0],i[0])
                ans[-1][1]=max(ans[-1][1],i[1])
        return ans