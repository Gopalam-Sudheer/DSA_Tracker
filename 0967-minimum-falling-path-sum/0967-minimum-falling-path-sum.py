class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                temp=matrix[i-1][j]
                if j-1>=0:
                    temp=min(temp,matrix[i-1][j-1])
                if j+1<len(matrix[0]):
                    temp=min(temp,matrix[i-1][j+1])
                matrix[i][j]+=temp
        return min(matrix[-1])