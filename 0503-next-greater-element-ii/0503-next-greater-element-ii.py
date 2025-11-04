class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st=[]
        ans=[-1]*len(nums)
        for i in range(2*len(nums)-1,-1,-1):
            ind=i%len(nums)
            while st and nums[ind]>=st[-1]:
                st.pop()
            if i<len(nums):
                if st:
                    ans[i]=st[-1]
            st.append(nums[ind])
        return ans