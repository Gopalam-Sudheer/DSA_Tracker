class Solution {
    public boolean isValid(String word) {
        if(word.length()<3){
            return false;
        }
        boolean v=false;
        boolean c=false;
        for(char ch : word.toCharArray()){
            if(Character.isLetter(ch)){
                char chr=Character.toLowerCase(ch);
                if(chr=='a' || chr=='e' || chr=='i' || chr=='o' || chr=='u'){
                    v=true;
                }else{
                    c=true;
                }
            }else if(!Character.isDigit(ch)){
                return false;
            }
        }
        return v&c;
    }
}
        