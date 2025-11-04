class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for i in num:
            if len(st)==0:
                st.append(i)
                continue
            while k>0 and st and st[-1]>i:
                k-=1
                st.pop()
            st.append(i)
        while st and k>0:
            st.pop()
            k-=1
        ind=0
        while ind<len(st) and st[ind]=='0':
            ind+=1
        if ind==len(st):
            return '0'
        else:
            return "".join(st[ind:])