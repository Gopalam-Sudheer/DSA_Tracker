class Solution {
    public int maximumLength(int[] nums) {
        int odd=0;
        int even=0;
        int prev=-1;
        int alt=0;
        for(int i: nums){
            if(i%2==0){
                even+=1;
            }else{
                odd+=1;
            }
            if(prev==-1 || (prev&1)!=(i&1)){
                prev=i;
                alt+=1;
            }
        }
        return Math.max(Math.max(odd,even),alt);
    }
}