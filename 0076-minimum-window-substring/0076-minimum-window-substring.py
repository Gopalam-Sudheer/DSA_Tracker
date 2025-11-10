class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d={}
        for i in t:
            d[i]=d.get(i,0)+1
        start=0
        end=0
        n=len(s)
        ans=float('inf')
        res=""
        c=0
        while end<n:
            d[s[end]]=d.get(s[end],0)-1
            if d[s[end]]>=0:
                c+=1
            while c>=len(t):
                if end-start+1<ans:
                    res=s[start:end+1]
                    ans=end-start+1
                d[s[start]]+=1
                if d[s[start]]>0:
                    c-=1
                start+=1
            end+=1
        return res