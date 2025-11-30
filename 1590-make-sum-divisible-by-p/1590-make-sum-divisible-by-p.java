class Solution {
    public int minSubarray(int[] nums, int p) {
        HashMap<Integer,Integer> hp=new HashMap<>();
        int m=0;
        for(int i=0;i<nums.length;i++){
            m=(m+nums[i])%p;
        }
        if(m==0){
            return 0;
        }
        int prefix=0;
        int ans=nums.length;
        hp.put(0,-1);
        for(int i=0;i<nums.length;i++){
            prefix=(prefix+nums[i])%p;
            if(hp.containsKey((prefix-m+p)%p)){
                ans=Math.min(ans,i-hp.get((prefix-m+p)%p));
            }
            hp.put(prefix,i);
        }
        if(ans==nums.length){
            return -1;
        }
        return ans;
    }
}