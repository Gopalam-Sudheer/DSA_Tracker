class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums2)
        st=[]
        for i in range(len(nums2)-1,-1,-1):
            while st and nums2[i]>=st[-1]:
                st.pop()
            if len(st)==0:
                ans[i]=-1
            else:
                ans[i]=st[-1]
            st.append(nums2[i])
        res=[]
        for i in nums1:
            ind=nums2.index(i)
            res.append(ans[ind])
        return res