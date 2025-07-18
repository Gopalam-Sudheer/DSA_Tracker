class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,r,u,d=0,len(matrix[0])-1,0,len(matrix)-1
        ans=[]
        p=0
        while l<=r and u<=d:
            p=p%4
            if p==0:
                for i in range(l,r+1):
                    ans.append(matrix[u][i])
                u+=1
            elif p==1:
                for i in range(u,d+1):
                    ans.append(matrix[i][r])
                r-=1
            elif p==2:
                for i in range(r,l-1,-1):
                    ans.append(matrix[d][i])
                d-=1
            elif p==3:
                for i in range(d,u-1,-1):
                    ans.append(matrix[i][l])
                l+=1
            p=p+1
        return ans