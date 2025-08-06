class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        ans=0
        start=0
        for i in range(len(s)):
            if s[i] in d and d[s[i]]>=start:
                start=d[s[i]]+1
            d[s[i]]=i
            ans=max(ans,i-start+1)
        return ans
        