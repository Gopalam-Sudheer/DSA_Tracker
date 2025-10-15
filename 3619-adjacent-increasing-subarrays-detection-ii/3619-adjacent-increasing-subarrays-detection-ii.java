class Solution {
    public int maxIncreasingSubarrays(List<Integer> nums) {
        List<Integer> arr=new ArrayList<>();
        int cur=1;
        for(int i=1;i<nums.size();i++){
            if(nums.get(i-1)<nums.get(i)){
                cur+=1;
            }else{
                arr.add(cur);
                cur=1;
            }
        }
        if(cur>0){
            arr.add(cur);
        }
        int maxi=arr.get(0);
        int ans=0;
        for(int ind=1;ind<arr.size();ind++){
            if(arr.get(ind)>maxi){
                maxi=arr.get(ind);
            }
            if(Math.min(arr.get(ind-1),arr.get(ind))>ans){
                ans=Math.min(arr.get(ind-1),arr.get(ind));
            }
        }
        return Math.max(maxi/2,ans);
    }
}