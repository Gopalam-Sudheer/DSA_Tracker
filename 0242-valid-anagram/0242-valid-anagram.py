class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        occ=[0 for i in range(26)]
        for i in range(len(s)):
            occ[ord(s[i])-ord('a')]+=1
            occ[ord(t[i])-ord('a')]-=1
        for i in occ:
            if i!=0:
                return False
        return True