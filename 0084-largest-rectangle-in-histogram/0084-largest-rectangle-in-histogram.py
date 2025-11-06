class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[]
        ans=0
        for i in range(len(heights)):
            while st and heights[st[-1]]>=heights[i]:
                ind=st.pop()
                if st:
                    ans=max(ans,(i-st[-1]-1)*heights[ind])
                else:
                    ans=max(ans,(i)*heights[ind])
            st.append(i)
        nex=len(heights)
        while st:
            curr=st.pop()
            if st:
                pre=st[-1]
            else:
                pre=-1
            ans=max(ans,(nex-pre-1)*heights[curr])
        return ans