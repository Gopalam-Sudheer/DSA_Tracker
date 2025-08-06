class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        d={}
        for i in s1:
            d[i]=d.get(i,0)+1
        c=0
        start=0
        end=0
        while end<len(s2):
            d[s2[end]]=d.get(s2[end],0)-1
            if d[s2[end]]>=0:
                c+=1
            if end-start+1>len(s1):
                d[s2[start]]+=1
                if d[s2[start]]>0:
                    c-=1
                start+=1
            if c==len(s1):
                return True
            end+=1
        return False