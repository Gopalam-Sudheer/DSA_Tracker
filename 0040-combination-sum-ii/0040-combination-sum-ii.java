class Solution {
    public void gen(List<List<Integer>> ans,List<Integer> arr,int index,int[] candidates,int target){
        if(target==0){
            ans.add(new ArrayList<>(arr));
            return;
        }
        if(target<0 || index==candidates.length){
            return;
        }
        arr.add(candidates[index]);
        gen(ans,arr,index+1,candidates,target-candidates[index]);
        arr.remove(arr.size()-1);
        for(int i=index+1;i<candidates.length;i++){
            if(candidates[i]!=candidates[index]){
                gen(ans,arr,i,candidates,target);
                break;
            }
        }
    }
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> ans= new ArrayList<>();
        List<Integer> arr=new ArrayList<>();
        Arrays.sort(candidates);
        gen(ans,arr,0,candidates,target);
        return ans;
    }
}