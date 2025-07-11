class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        d={}
        for i in strs:
            l=[0 for r in range(26)]
            for j in range(len(i)):
                l[ord(i[j])-ord('a')]+=1
            s=""
            for k in range(len(l)):
                s+=l[k]*chr(ord('a')+k)
            if s in d:
                d[s].append(i)
            else:
                d[s]=[i]
        for i in d:
            ans.append(d[i])
        return ans
        

