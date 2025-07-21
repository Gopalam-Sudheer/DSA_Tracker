class Solution:
    def nSet(self,k,n,val,ans,store,s):
        if len(store)>k or s>n:
            return
        if val==0:
            if s==n and len(store)==k:
                ans.append(store[:])
            return
        store.append(val)
        self.nSet(k,n,val-1,ans,store,s+val)
        store.pop()
        self.nSet(k,n,val-1,ans,store,s)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        self.nSet(k,n,9,ans,[],0)
        return ans