class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(i,j,mat,visited,q):
            if i>=0 and i<len(mat) and j>=0 and j<len(mat[0]) and mat[i][j]=='O' and visited[i][j]==False:
                visited[i][j]=True
                q.append((i,j))
        mat=board
        q=deque()
        visited=[[False for i in range(len(mat[0]))] for j in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]=='O' and (i==0 or i==len(mat)-1 or j==0 or j==len(mat[0])-1):
                    visited[i][j]=True
                    q.append((i,j))
        while len(q)!=0:
            row,col=q.popleft()
            isValid(row+1,col,mat,visited,q)
            isValid(row-1,col,mat,visited,q)
            isValid(row,col+1,mat,visited,q)
            isValid(row,col-1,mat,visited,q)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]=='O' and visited[i][j]==False:
                    mat[i][j]='X'
        # return mat


                                                                                                                                                                                                                                                                                                     
        