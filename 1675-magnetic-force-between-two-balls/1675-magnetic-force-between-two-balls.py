class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def helper(arr,d):
            balls=1
            last=arr[0]
            for i in range(1,len(arr)):
                if abs(arr[i]-last)>=d:
                    last=arr[i]
                    balls+=1
            return balls
        low=1
        high=max(position)
        while low<=high:
            mid=(low+high)//2
            valid=helper(position,mid)
            if valid<m:
                high=mid-1
            else:
                ans=mid
                low=mid+1
        return ans
                
