class Solution {
    public int changer(String s){
        String[] arr=s.split(":");
        return Integer.parseInt(arr[0])*60+Integer.parseInt(arr[1]);
    }
    public List<String> alertNames(String[] keyName, String[] keyTime) {
        List<String> ans=new ArrayList<>();
        Map<String,List<Integer>> mp=new HashMap<>();
        for(int i=0;i<keyName.length;i++){
            if(!mp.containsKey(keyName[i])){
                mp.put(keyName[i],new ArrayList<>());
            }
            mp.get(keyName[i]).add(changer(keyTime[i]));
        } 
        for(String s: mp.keySet()){
            List<Integer> list=mp.get(s);
            Collections.sort(list);
            for(int i=0;i+2<list.size();i++){
                if(list.get(i+2)-list.get(i)<=60){
                    ans.add(s);
                    break;
                }
            }
        }
        Collections.sort(ans);
        return ans;
    }
}