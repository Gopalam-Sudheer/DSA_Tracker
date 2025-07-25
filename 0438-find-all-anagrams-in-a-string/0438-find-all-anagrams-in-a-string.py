class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        if len(s)<len(p):
            return ans
        d={}
        c=0
        for i in p:
            d[i]=d.get(i,0)+1
        for i in range(len(p)):
            d[s[i]]=d.get(s[i],0)-1
            if d[s[i]]>=0:
                c+=1
        if c==len(p):
            ans.append(0)
        for i in range(len(p),len(s)):
            d[s[i]]=d.get(s[i],0)-1
            if d[s[i]]>=0:
                c+=1
            d[s[i-len(p)]]=d.get(s[i-len(p)],0)+1
            if d[s[i-len(p)]]>0:
                c-=1
            if c==len(p):
                ans.append(i-len(p)+1)
        return ans
            

        return ans
            
