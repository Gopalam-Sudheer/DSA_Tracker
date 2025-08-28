class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isValid(i,j,grid,visited,q):
            if i>=0 and i<len(grid) and j>=0 and j<len(grid[0]) and grid[i][j]==1 and visited[i][j]==False:
                visited[i][j]=True
                q.append((i,j))
                return True
            return False
        ans=0
        q=deque()
        visited=[[False for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    visited[i][j]=True
                    q.append((i,j))
        while len(q)!=0:
            ans+=1
            l=len(q)
            for i in range(l):
                a,b=q.popleft()
                isValid(a+1,b,grid,visited,q)
                isValid(a-1,b,grid,visited,q)
                isValid(a,b+1,grid,visited,q)
                isValid(a,b-1,grid,visited,q)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and visited[i][j]==False:
                    return -1
        if ans==0:
            return 0
        return ans-1

                                                                                                                                                                                                                                                                                                                                                                                                                                
