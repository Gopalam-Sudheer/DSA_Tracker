class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans=0
        start=0
        end=0
        d={}
        maxi=0
        while end<len(s):
            d[s[end]]=d.get(s[end],0)+1
            maxi=max(maxi,d[s[end]])
            if end-start+1-maxi<=k:
                ans=max(ans,end-start+1)
            else:
                d[s[start]]-=1
                start+=1
            end+=1
        return ans
                