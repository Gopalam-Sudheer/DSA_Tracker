class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        d={}
        for s in strs:
            occ=[0 for i in range(26)]
            for c in s:
                occ[ord(c)-ord('a')]+=1
            key=""
            for i in range(26):
                key+=chr(ord('a')+i)*occ[i]
            if key in d:
                d[key].append(s)
            else:
                d[key]=[s]
        for i in d:
            ans.append(d[i])
        return ans
        