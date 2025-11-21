class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        List<String> list=new ArrayList<>();
        Map<String,Integer> frequency=new HashMap<>();
        for(int i=0;i<=s.length()-10;i++){
            String sub=s.substring(i,i+10);
            frequency.put(sub,frequency.getOrDefault(sub,0)+1);
        }
        for(Map.Entry<String,Integer> item : frequency.entrySet()){
            if(item.getValue()>1){
                list.add(item.getKey());
            }
        }
        return list;
    }
}