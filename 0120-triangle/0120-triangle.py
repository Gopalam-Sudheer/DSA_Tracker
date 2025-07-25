class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)):
            for j in range(i+1):
                if i==0:
                    continue
                if j==0:
                    t=triangle[i-1][j]
                elif j==i:
                    t=triangle[i-1][j-1]
                else:
                    t=min(triangle[i-1][j],triangle[i-1][j-1])
                triangle[i][j]+=t
        return min(triangle[-1])
        