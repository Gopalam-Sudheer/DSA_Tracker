class Solution:
    def genComb(self,digits,vals,ind,temp,ans):
        if ind==len(digits):
            ans.append(temp)
            return
        for i in vals[int(digits[ind])]:
            self.genComb(digits,vals,ind+1,temp+i,ans)

    def letterCombinations(self, digits: str) -> List[str]:
        vals=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        ans=[]
        if len(digits)==0:
            return ans
        self.genComb(digits,vals,0,"",ans)
        return ans