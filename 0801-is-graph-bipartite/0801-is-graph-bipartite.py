class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs(visited,adj,k):
            q=deque()
            q.append(k)
            assign=0
            while len(q)!=0:
                l=len(q)
                for i in range(l):
                    a=q.popleft()
                    visited[a]=assign
                    for j in adj[a]:
                        if visited[j]==-1:
                            visited[j]=1-visited[a]
                            q.append(j)
                        elif visited[j]==visited[a]:
                            return False 
                assign=1-assign
            return True
        V=len(graph)
        visited=[-1 for i in range(V)]
        ans=True
        adj=graph
        for i in range(V):
            if visited[i]==-1:
                ans=(ans and bfs(visited,adj,i))
        return ans
        