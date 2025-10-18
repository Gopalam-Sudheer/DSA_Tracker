class Solution {
    public int maxDistinctElements(int[] nums, int k) {
        Arrays.sort(nums);
        nums[0]-=k;
        int ans=1;
        for(int i=1;i<nums.length;i++){
            int val=Math.max(nums[i-1]+1,nums[i]-k);
            if(val<=nums[i]+k){
                ans+=1;
                nums[i]=val;
            }else{
                nums[i]+=k;
            }
        }
        return ans;
    }
}