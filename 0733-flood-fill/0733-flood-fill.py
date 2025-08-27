class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        newColor=color
        visited=[[False for i in range(len(image[0]))] for j in range(len(image))]
        q=deque()
        oldColor=image[sr][sc]
        q.append((sr,sc))
        visited[sr][sc]=True
        image[sr][sc]=newColor
        while len(q)!=0:
            row,col=q.popleft()
            if row+1<len(image) and image[row+1][col]==oldColor and visited[row+1][col]==False:
                visited[row+1][col]=True
                q.append((row+1,col))
                image[row+1][col]=newColor
            if row-1>=0 and image[row-1][col]==oldColor and visited[row-1][col]==False:
                visited[row-1][col]=True
                q.append((row-1,col))
                image[row-1][col]=newColor
            if col+1<len(image[0]) and image[row][col+1]==oldColor and visited[row][col+1]==False:
                visited[row][col+1]=True
                q.append((row,col+1))
                image[row][col+1]=newColor
            if col-1>=0 and image[row][col-1]==oldColor and visited[row][col-1]==False:
                visited[row][col-1]=True
                q.append((row,col-1))
                image[row][col-1]=newColor
        return image