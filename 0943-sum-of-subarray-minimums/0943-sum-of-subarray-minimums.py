class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def pse(arr,ans):
            st=[]
            for i in range(len(arr)):
                while st and arr[st[-1]]>=arr[i]:
                    st.pop()
                if st:
                    ans[i]=st[-1]
                st.append(i)
        def nse(arr,ans):
            st=[]
            for i in range(len(arr)-1,-1,-1):
                while st and arr[st[-1]]>arr[i]:
                    st.pop()
                if st:
                    ans[i]=st[-1]
                st.append(i)
        pre=[-1]*len(arr)
        suff=[len(arr)]*len(arr)
        pse(arr,pre)
        nse(arr,suff)
        ans=0
        mod=1000000007
        for i in range(len(arr)):
            ans=(ans+(i-pre[i])*(suff[i]-i)*arr[i])%mod
        return ans
        