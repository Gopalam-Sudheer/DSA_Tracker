class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #your code goes here
        d={}
        c=0
        ans=float('inf')
        for i in t:
            d[i]=d.get(i,0)+1
        l=0
        r=0
        res=""
        while r<len(s):
            d[s[r]]=d.get(s[r],0)-1
            if d[s[r]]>=0:
                c+=1
            while c==len(t):
                d[s[l]]+=1
                if d[s[l]]>0:
                    c-=1
                if r-l+1<ans:
                    res=s[l:r+1]
                    ans=r-l+1
                l+=1
            r+=1
        return res
                                                                                                                                                                                                                   