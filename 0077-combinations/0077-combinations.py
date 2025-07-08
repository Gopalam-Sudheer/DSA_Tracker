class Solution:
    def combGen(self,ans,n,k,ind,temp):
        if len(temp)==k:
            ans.append(temp[:])
            return
        if ind==n+1:
            return
        temp.append(ind)
        self.combGen(ans,n,k,ind+1,temp)
        temp.pop()
        self.combGen(ans,n,k,ind+1,temp)

        

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        self.combGen(ans,n,k,1,[])
        return ans