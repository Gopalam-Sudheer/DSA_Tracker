class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        ans=0
        d={}
        maxi=0
        while r<len(s):
            d[s[r]]=d.get(s[r],0)+1
            maxi=max(maxi,d[s[r]])
            if r-l+1-maxi<=k:
                ans=max(ans,r-l+1)
            else:
                d[s[l]]-=1
                l+=1
            r+=1
        return ans