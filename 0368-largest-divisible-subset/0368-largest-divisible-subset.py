class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        arr=nums
        arr.sort()
        has=[i for i in range(len(arr))]
        lon=[ 1 for i in range(len(arr))]
        maxi=0
        for i in range(1,len(arr)):
            for j in range(i):
                if arr[i]%arr[j]==0 and lon[j]+1>lon[i]:
                    lon[i]=lon[j]+1
                    has[i]=j
                    if lon[i]>lon[maxi]:
                        maxi=i
        ans=[]
        while has[maxi]!=maxi:
            ans=[arr[maxi]]+ans
            maxi=has[maxi]
        ans=[arr[maxi]]+ans
        return ans