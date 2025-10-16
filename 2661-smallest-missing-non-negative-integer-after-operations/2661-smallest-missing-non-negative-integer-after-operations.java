class Solution {
    public int findSmallestInteger(int[] nums, int value) {
        int[] arr=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            int ind=nums[i]%value;
            if(ind>=0 && ind<nums.length){
                arr[ind]+=1;
            }else if(ind<0 && ind+value<nums.length){
                arr[ind+value]+=1;
            }
        }
        System.out.println(Arrays.toString(arr));
        for(int ind=0;ind<nums.length;ind++){
            if(arr[ind]==0){
                return ind;
            }else if(ind+value<arr.length){
                arr[ind+value]+=arr[ind]-1;
            }
        }
        return nums.length;
    }
}