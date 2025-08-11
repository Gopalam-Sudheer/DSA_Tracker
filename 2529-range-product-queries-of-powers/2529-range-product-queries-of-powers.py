class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        two_powers=[]
        val=0
        while n!=0:
            rem=n%2
            if rem==1:
                two_powers.append(2**val)
            val+=1
            n//=2
        ans=[]
        mod=1000000007
        for i in range(1,len(two_powers)):
            two_powers[i]=(two_powers[i]*two_powers[i-1])%mod
        for start,end in queries:
            if start==0:
                ans.append(two_powers[end])
            else:
                result = (two_powers[end] * pow(two_powers[start-1], mod-2, mod)) % mod
                ans.append(result)
        return ans