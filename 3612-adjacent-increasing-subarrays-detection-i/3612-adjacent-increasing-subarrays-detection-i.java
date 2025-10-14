class Solution {
    public boolean check(int i,int j,List<Integer> arr,int k){
        for(int ind=i+1;ind<i+k;ind++){
            if(arr.get(ind)<=arr.get(ind-1)){
                return false;
            }
        }
        for(int ind1=j+1;ind1<j+k;ind1++){
            if(arr.get(ind1)<=arr.get(ind1-1)){
                return false;
            }
        }
        return true; 
    }
    public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
        int prev=0;
        int cur=1;
        for(int i=0;i<nums.size()-2*k+1;i++){
            if(check(i,i+k,nums,k)){
                return true;
            }
        }
        return false;
    }
}