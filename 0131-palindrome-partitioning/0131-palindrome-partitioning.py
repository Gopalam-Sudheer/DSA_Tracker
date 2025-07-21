class Solution:
    def fun(self,s,ind,store,ans):
        if ind==len(s):
            ans.append(store[:])
            return
        for i in range(ind+1,len(s)+1):
            temp=s[ind:i]
            if temp==temp[::-1]:
                store.append(temp)
                self.fun(s,i,store,ans)
                store.pop()
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        self.fun(s,0,[],ans)
        return ans