class Solution {
    public int climbStairs(int n) {
        if(n<=2){
            return n;
        }
        int prev=1;
        int curr=2;
        for(int i=0;i<n-2;i++){
            int nex=prev+curr;
            prev=curr;
            curr=nex;
        }
        return curr;
    }
}