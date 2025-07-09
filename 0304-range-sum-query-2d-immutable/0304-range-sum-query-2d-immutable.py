class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.preSum=[]
        for i in range(len(matrix)):
            temp=[]
            cur=0
            for j in matrix[i]:
                cur+=j
                temp.append(cur)
            self.preSum.append(temp[:])


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=0
        for j in range(row1,row2+1):
            if col1==0:
                ans+=self.preSum[j][col2]
            else:
                ans+=self.preSum[j][col2]-self.preSum[j][col1-1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)