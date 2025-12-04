class Solution {
    public int countCollisions(String directions) {
        int start=0;
        int end=directions.length()-1;
        int ans=0;
        while(start<=end && directions.charAt(start)=='L'){
            start+=1;
        } 
        while(end>=start && directions.charAt(end)=='R'){
            end-=1;
        }
        if(start<=end){
            for(int i=start;i<=end;i++){
                if(directions.charAt(i)!='S'){
                    ans+=1;
                }
            }
        }
        return ans;
    }
}