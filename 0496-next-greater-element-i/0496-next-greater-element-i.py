class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        d={}
        result=[]
        for i in range(len(nums2)-1,-1,-1):
            while len(st)!=0 and st[-1]<nums2[i]:
                st.pop()
            if len(st)==0:
                d[nums2[i]]=-1
            else:
                d[nums2[i]]=st[-1]
            st.append(nums2[i])
        for j in nums1:
            result.append(d[j])
        return result
        