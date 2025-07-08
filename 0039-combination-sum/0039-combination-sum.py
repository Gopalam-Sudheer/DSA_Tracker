class Solution:
    def combGen(self,ans,temp,ind,target,candidates,s):
        if s>target or ind==len(candidates):
            return
        if s==target:
            ans.append(temp[:])
            return
        temp.append(candidates[ind])
        self.combGen(ans,temp,ind,target,candidates,s+candidates[ind])
        temp.pop()
        self.combGen(ans,temp,ind+1,target,candidates,s)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        self.combGen(ans,[],0,target,candidates,0)
        return ans