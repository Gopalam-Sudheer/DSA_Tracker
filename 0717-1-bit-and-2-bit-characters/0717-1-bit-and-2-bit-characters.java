class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int ind=0;
        boolean ans=true;
        while(ind<bits.length){
            if(bits[ind]==1){
                ind+=2;
                ans=false;
            }else{
                ind+=1;
                ans=true;
            }
        }
        return ans;
    }
}