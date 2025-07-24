class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for i in num:
            while k>0 and len(st)>0 and st[-1]>i:
                st.pop()
                k-=1
            st.append(i)
        for i in range(k):
            st.pop()
        res=''.join(st)
        res=res.lstrip('0')
        if len(res)==0:
            return "0"
        return res