class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int cur=0;
        int ans=0;
        for(int i : nums){
            if(i==1){
                cur+=1;
                ans=Math.max(cur,ans);
            }else{
                cur=0;
            }
        }
        return ans;
    }
}