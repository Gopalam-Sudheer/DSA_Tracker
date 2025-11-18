class Solution {
    public void gen(int ind,List<List<Integer>> ans,int[] arr,List<Integer> dup){
        if(ind==arr.length){
            ans.add(new ArrayList<>(dup));
            return;
        }
        dup.add(arr[ind]);
        gen(ind+1,ans,arr,dup);
        dup.remove(dup.size()-1);
        gen(ind+1,ans,arr,dup);
    }
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans=new ArrayList<>();
        List<Integer> dup= new ArrayList<>();
        gen(0,ans,nums,dup);
        return ans;
    }
}