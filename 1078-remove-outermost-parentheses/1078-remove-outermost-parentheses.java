class Solution {
    public String removeOuterParentheses(String s) {
        String ans="";
        int start=0;
        int end=0;
        int open=0,close=0;
        while(end<s.length()){
            if(s.charAt(end)=='('){
                open+=1;
            }else{
                close+=1;
            }
            if(open==close){
                ans+=s.substring(start+1,end);
                start=end+1;
            }
             end+=1;
        }
        return ans;
    }
}