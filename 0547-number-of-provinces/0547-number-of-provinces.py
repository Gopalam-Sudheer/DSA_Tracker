class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs(i,adj,visited):
            visited[i]=True
            q=deque()
            q.append(i)
            while len(q)!=0:
                num=q.popleft()
                for i in range(len(adj)):
                    if adj[num][i]==1 and num!=i and visited[i]==False:
                        q.append(i)
                        visited[i]=True
        adj=isConnected
        n=len(adj)
        visited=[False for i in range(n)]
        ans=0
        for i in range(n):
            if visited[i]==False:
                ans+=1
                bfs(i,adj,visited)
        return ans

                                                                                                                                                                                                                                                                            