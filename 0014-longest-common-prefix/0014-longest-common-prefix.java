class Solution {
    public String fun(String s1,String s2){
        int i=0;
        int j=0;
        while(i<s1.length() && j<s2.length()){
            if(s1.charAt(i)==s2.charAt(j)){
                i+=1;
                j+=1;
            }else{
                return s1.substring(0,i);
            }
        }
        return s1.substring(0,i);
    }
    public String longestCommonPrefix(String[] strs) {
        if(strs.length==0){
            return "";
        }
        String ans=strs[0];
        for(int i=1;i<strs.length;i++){
            ans=fun(ans,strs[i]);
        }
        return ans;
    }
}