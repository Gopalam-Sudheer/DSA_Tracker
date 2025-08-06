class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            start=i+1
            end=len(nums)-1
            while start<end:
                if nums[start]+nums[end]==-1*nums[i]:
                    ans.append([nums[i],nums[start],nums[end]])
                    start+=1
                    end-=1
                    while start<end and nums[start]==nums[start-1]:
                        start+=1
                    while start<end and nums[end]==nums[end+1]:
                        end-=1
                elif nums[start]+nums[end]>-1*nums[i]:
                    end-=1
                else:
                    start+=1
        return ans
        