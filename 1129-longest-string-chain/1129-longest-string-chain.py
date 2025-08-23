class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def helper(s1,s2):
            if len(s1)!=len(s2)+1:
                return False
            i=0
            j=0
            while i<len(s1):
                if j<len(s2) and s1[i]==s2[j]:
                    j+=1
                i+=1
            if i==len(s1) and j==len(s2):
                return True
            return False
        arr=words
        arr.sort(key=len)
        lon=[ 1 for i in range(len(arr))]
        maxi=1
        for i in range(1,len(arr)):
            for j in range(i):
                if helper(arr[i],arr[j]) and lon[j]+1>lon[i]:
                    lon[i]=lon[j]+1
                if lon[i]>maxi:
                    maxi=lon[i]
        return maxi
        