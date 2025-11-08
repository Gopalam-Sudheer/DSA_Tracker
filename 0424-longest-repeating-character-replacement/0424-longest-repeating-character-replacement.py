class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        start=0
        end=0
        ans=0
        n=len(s)
        maxi=0
        while end<n:
            d[s[end]]=d.get(s[end],0)+1
            maxi=max(maxi,d[s[end]])
            if end-start+1-maxi<=k:
                ans=max(ans,end-start+1)
            else:
                d[s[start]]-=1
                start+=1
            end+=1
        return ans