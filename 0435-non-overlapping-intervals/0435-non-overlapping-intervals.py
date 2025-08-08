class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair: pair[0])
        prev=intervals[0][1]
        res=0
        for i in intervals[1:]:
            if prev<=i[0]:
                prev=i[1]
            else:
                res+=1
                prev=min(prev,i[1])
        return res


        