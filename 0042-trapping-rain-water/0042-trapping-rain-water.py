class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        left=0
        right=len(height)-1
        maxL=height[0]
        maxR=height[len(height)-1]
        while left<=right:
            maxL=max(maxL,height[left])
            maxR=max(maxR,height[right])
            if height[left]<height[right]:
                ans+=max(0,min(maxL,maxR)-height[left])
                left+=1
            else:
                ans+=max(0,min(maxL,maxR)-height[right])
                right-=1
        return ans
        