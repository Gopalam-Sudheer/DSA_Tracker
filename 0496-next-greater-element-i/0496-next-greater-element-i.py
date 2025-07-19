class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        ans=[0]*len(nums2)
        result=[]
        for i in range(len(nums2)-1,-1,-1):
            while len(st)!=0 and st[-1]<nums2[i]:
                st.pop()
            if len(st)==0:
                ans[i]=-1
            else:
                ans[i]=st[-1]
            st.append(nums2[i])
        print(ans)
        for j in nums1:
            result.append(ans[nums2.index(j)])
        return result
        