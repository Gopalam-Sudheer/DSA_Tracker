class Solution:
    def printSubsets(self,ans,arr,ind,temp):
        if ind==len(arr):
            ans.append(temp[:])
            return
        self.printSubsets(ans,arr,ind+1,temp)
        temp.append(arr[ind])
        self.printSubsets(ans,arr,ind+1,temp)
        temp.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        self.printSubsets(ans,nums,0,[])
        return ans