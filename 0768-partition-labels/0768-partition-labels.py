class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        ans=[]
        for i in range(len(s)):
            d[s[i]]=i
        maxi=0
        for i in range(len(s)):
            maxi=max(maxi,d[s[i]])
            if i==maxi:
                ans.append(i+1)
        for i in range(len(ans)-1,0,-1):
            ans[i]-=ans[i-1]
        return ans
        