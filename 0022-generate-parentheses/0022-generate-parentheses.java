class Solution {
    public void gen(int open,int close,int n,String s, List<String> ans){
        if(open+close==2*n){
            if(open==close){
                ans.add(s);
            }
            return;
        }
        if(open<close || open>n){
            return;
        }
        gen(open+1,close,n,s+"(",ans);
        gen(open,close+1,n,s+")",ans);
    }
    public List<String> generateParenthesis(int n) {
        List<String> ans=new ArrayList<>();
        gen(0,0,n,"",ans);
        return ans;
    }
}