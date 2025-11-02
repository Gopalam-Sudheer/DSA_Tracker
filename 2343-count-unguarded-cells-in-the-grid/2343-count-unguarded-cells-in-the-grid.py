class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def helper(grid,i,j):
            x,y=i-1,j-1
            while x>=0 and grid[x][j]!='G' and grid[x][j]!='W':
                grid[x][j]='X'
                x-=1
            while y>=0 and grid[i][y]!='G' and grid[i][y]!='W':
                grid[i][y]='X'
                y-=1
            x,y=i+1,j+1
            while x<len(grid) and grid[x][j]!='G' and grid[x][j]!='W':
                grid[x][j]='X'
                x+=1
            while y<len(grid[0]) and grid[i][y]!='G' and grid[i][y]!='W':
                grid[i][y]='X'
                y+=1

        grid=[['' for j in range(n)] for i in range(m)]
        for i in guards:
            grid[i[0]][i[1]]='G'
        for i in walls:
            grid[i[0]][i[1]]='W'
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='G':
                    helper(grid,i,j)
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='':
                    ans+=1
        return ans
        