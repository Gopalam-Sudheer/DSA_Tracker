class Solution:
    def combGen(self,ans,n,k,ind,temp):
        if len(temp)==k:
            ans.append(temp[:])
            return
        if ind==n+1:
            return
        for i in range(ind,n+1):
            temp.append(i)
            self.combGen(ans,n,k,i+1,temp)
            temp.pop()        

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        self.combGen(ans,n,k,1,[])
        return ans