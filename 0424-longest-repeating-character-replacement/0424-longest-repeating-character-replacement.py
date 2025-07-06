class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans=0
        charCount={}
        start=0
        end=0
        maxFreq=0
        while end<len(s):
            charCount[s[end]]=1+charCount.get(s[end],0)
            maxFreq=max(maxFreq,charCount[s[end]])
            if end-start+1-maxFreq<=k:
                ans=max(ans,end-start+1)
            else:
                charCount[s[start]]-=1
                start+=1
            end+=1
        return ans