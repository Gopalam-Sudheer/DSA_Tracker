class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        st=[]
        preSmall=[-1 for i in range(len(arr))]
        postSmall=[len(arr)]*len(arr)
        ans=0
        for i in range(len(arr)):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()
            if st:
                preSmall[i]=st[-1]
            st.append(i)
        st=[]
        for i in range(len(arr)-1,-1,-1):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
            if st:
                postSmall[i]=st[-1]
            st.append(i)
            ans=(ans+(i-preSmall[i])*(postSmall[i]-i)*arr[i])%1000000007
        return ans%1000000007