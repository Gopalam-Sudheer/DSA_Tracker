class Solution {
    public void gen(String digits,int index,String[] map,List<String> ans,String s){
        if(index==digits.length()){
            ans.add(s);
            return;
        }
        for(char c: map[digits.charAt(index)-'0'].toCharArray()){
            gen(digits,index+1,map,ans,s+c);
        }
    }
    public List<String> letterCombinations(String digits) {
        String[] map={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        List<String> ans=new ArrayList<>();
        gen(digits,0,map,ans,"");
        return ans;
    }
}