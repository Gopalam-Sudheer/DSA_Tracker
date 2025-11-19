class Solution {
    public void bfs(int node,int[][] isConnected,boolean[] visited){
        Queue<Integer> q=new LinkedList<>();
        q.add(node);
        visited[node]=true;
        while(!q.isEmpty()){
            int curr=q.poll();
            for(int i=0;i<isConnected[curr].length;i++){
                if(isConnected[curr][i]==1 && visited[i]==false){
                    visited[i]=true;
                    q.add(i);
                }
            }
        }
    }
    public int findCircleNum(int[][] isConnected) {
        int n=isConnected.length;
        boolean[] visited=new boolean[n];
        int ans=0;
        for(int i=0;i<n;i++){
            if(!visited[i]){
                bfs(i,isConnected,visited);
                ans++;
            }
        }
        return ans;
    }
}