class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        d={}
        result=[]
        for i in nums2:
            while st and st[-1]<i:
                d[st.pop()]=i
            st.append(i)
        for i in st:
            d[i]=-1
        return [d[x] for x in nums1]
        