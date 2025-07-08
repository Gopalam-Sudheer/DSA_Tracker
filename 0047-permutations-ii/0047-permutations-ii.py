class Solution:
    def genPerm(self,cou,ans,ind,temp,k):
        if k==len(temp):
            ans.append(temp[:])
            return
        for i in cou:
            if cou[i]>0:
                cou[i]-=1
                temp.append(i)
                self.genPerm(cou,ans,ind+1,temp,k)
                cou[i]+=1
                temp.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        cou={}
        for i in nums:
            cou[i]=1+cou.get(i,0)
        self.genPerm(cou,ans,0,[],len(nums))
        return ans