class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def isValid(r,c,mat):
            if r<0 or c<0 or r==len(mat) or c==len(mat[0]):
                return False
            return True
        visited=[[False for i in range(len(image[0]))] for j in range(len(image))]
        q=deque()
        q.append((sr,sc))
        oldColor=image[sr][sc]
        x=[-1,0,1,0]
        y=[0,-1,0,1]
        while q:
            r,c=q.popleft()
            image[r][c]=color
            visited[r][c]=True
            for i in range(4):
                if isValid(r+x[i],c+y[i],image) and visited[r+x[i]][c+y[i]]==False and image[r+x[i]][c+y[i]]==oldColor:
                    q.append((r+x[i],c+y[i]))
        return image
