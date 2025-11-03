class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        start=0
        end=0
        total=0
        s=0
        while end<len(colors):
            total+=neededTime[end]
            if colors[start]!=colors[end]:
                s+=neededTime[start]
                start=end
            else:
                if neededTime[start]<neededTime[end]:
                    start=end
            end+=1
        s+=neededTime[start]
        return total-s