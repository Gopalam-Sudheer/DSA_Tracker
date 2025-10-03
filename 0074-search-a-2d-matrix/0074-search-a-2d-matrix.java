class Solution {
    public boolean searchMatrix(int[][] mat, int target) {
        int high=(mat.length*mat[0].length)-1;
        int low=0;
        while(low<=high){
            int mid=(low+high)/2;
            int row=mid/mat[0].length;
            int col=mid%mat[0].length;
            if(mat[row][col]==target){
                return true;
            }else if(mat[row][col]<target){
                low=mid+1;
            }else{
                high=mid-1;
            }
        }
        return false;
    }
}