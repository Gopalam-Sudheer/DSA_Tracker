class Solution {
    public int helper(int start,int end,int[] nums){
        if(end-start+1==1){
            return nums[start];
        }
        int first=nums[start];
        int second=Math.max(nums[start+1],first);
        for(int i=start+2;i<=end;i++){
            int temp=Math.max(second,nums[i]+first);
            first=second;
            second=temp;
        } 
        return second;
    }
    public int rob(int[] nums) {
        if(nums.length==1){
            return nums[0]; 
        }
        return Math.max(helper(0,nums.length-2,nums),helper(1,nums.length-1,nums));
    }
}