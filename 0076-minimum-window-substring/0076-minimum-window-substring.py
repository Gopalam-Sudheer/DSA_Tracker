class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #your code goes here
        d={}
        for i in t:
            d[i]=d.get(i,0)+1
        start=0
        end=0
        c=0
        ans=float('inf')
        res=""
        while end<len(s):
            d[s[end]]=d.get(s[end],0)-1
            if d[s[end]]>=0:
                c+=1
            while c>=len(t):
                if end-start+1<ans:
                    ans=end-start+1
                    res=s[start:end+1]
                d[s[start]]+=1
                if d[s[start]]>0:
                    c-=1
                start+=1
            end+=1
        return res
                                                                                                                                                                                                                   