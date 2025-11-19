class Solution {
    public int findFinalValue(int[] nums, int original) {
        Set<Integer> vals=new HashSet<>();
        for(int val: nums){
            vals.add(val);
        }
        while(vals.contains(original)){
            original*=2;
        }
        return original;
    }
}