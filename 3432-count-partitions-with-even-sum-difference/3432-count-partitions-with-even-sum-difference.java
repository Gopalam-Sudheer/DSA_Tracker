class Solution {
    public int countPartitions(int[] nums) {
        int sum=0;
        int left=0;
        for(int i:nums){
            sum+=i;
        }
        int ans=0;
        if(sum%2==0){
            ans-=1;
        }
        for(int i:nums){
            left+=i;
            sum-=i;
            if((sum-left)%2==0){
                ans+=1;
            }
        }
        return ans;
    }
}