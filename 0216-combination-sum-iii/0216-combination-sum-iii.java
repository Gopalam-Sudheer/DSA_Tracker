class Solution {
    public void comb(int k,int n,List<List<Integer>> ans,List<Integer> arr){
        if(n==0 && arr.size()==k){
            ans.add(new ArrayList<>(arr));
            return;
        }
        if(arr.size()>k || n<0){
            return;
        }
        int start;
        if(arr.size()==0){
            start=1;
        }else{
            start=arr.get(arr.size()-1)+1;
        }
        for(int i=start;i<10;i++){
            arr.add(i);
            comb(k,n-i,ans,arr);
            arr.remove(arr.size()-1);
        }
    }
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> ans=new ArrayList<>();
        List<Integer> arr=new ArrayList<>();
        comb(k,n,ans,arr);
        return ans;
    }
}