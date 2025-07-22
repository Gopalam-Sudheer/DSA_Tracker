class Solution:    
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        r=0
        ans=0
        d={}
        c=0
        d['a']=1
        d['b']=1
        d['c']=1
        while r<len(s):
            d[s[r]]-=1
            if d[s[r]]==0:
                c+=1
            while c==3:
                ans+=len(s)-r
                d[s[l]]+=1
                if d[s[l]]>0:
                    c-=1
                l+=1
            r+=1
        return ans