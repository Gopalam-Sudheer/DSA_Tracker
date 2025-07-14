class Solution {
    public void merge(int[] nums,int start,int mid,int end){
        int i=start;
        int j=mid+1;
        int k=0;
        int[] temp=new int[end-start+1];
        while(i<=mid && j<=end){
            if(nums[i]<nums[j]){
                temp[k]=nums[i];
                i+=1;
            }else{
                temp[k]=nums[j];
                j+=1;
            }
            k+=1;
        }
        while(i<=mid){
            temp[k]=nums[i];
            i+=1;
            k+=1;
        }
        while(j<=end){
            temp[k]=nums[j];
            j+=1;
            k+=1;
        }
        for(int c=start;c<=end;c++){
            nums[c]=temp[c-start];
        }
    }
    public void mergeSort(int[] nums,int start,int end){
        if(start>=end){
            return;
        }
        int mid=(start+end)/2;
        mergeSort(nums,start,mid);
        mergeSort(nums,mid+1,end);
        merge(nums,start,mid,end);
    }
    public int[] sortArray(int[] nums) {
        mergeSort(nums,0,nums.length-1);
        return nums;
    }
}