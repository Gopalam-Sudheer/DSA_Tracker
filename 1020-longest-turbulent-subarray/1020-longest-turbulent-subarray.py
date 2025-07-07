class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans=1
        sign='.'
        cur=1
        for i in range(1,len(arr)):
            if arr[i]<arr[i-1]:
                op='<'
            elif arr[i]>arr[i-1]:
                op='>'
            else:
                ans=max(ans,cur)
                cur=1
                sign='.'
                continue
            if op!=sign:
                sign=op
                cur+=1
            else:
                ans=max(ans,cur)
                cur=2
                continue
            ans=max(ans,cur)
        return ans