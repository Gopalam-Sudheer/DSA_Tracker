class Solution:
    def isTrue(self,d1,d2):
        if len(d2)>len(d1):
            return False
        for i in d2:
            if i not in d1 or d1[i]<d2[i]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        d1={}
        d2={}
        for i in t:
            d2[i]=1+d2.get(i,0)
        start=0
        end=0
        ans=s+s
        while end<len(s):
            d1[s[end]]=1+d1.get(s[end],0)
            while self.isTrue(d1,d2):
                if end-start+1<len(ans):
                    ans=s[start:end+1]
                d1[s[start]]-=1
                start+=1
            end+=1
        if ans==s+s:
            return ""
        else:
            return ans