class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        ans=0
        maxL,maxR=0,0
        i,j=0,len(height)-1
        while i<=j:
            maxL=max(height[i],maxL)
            maxR=max(height[j],maxR)
            if height[i]<height[j]:
                maxL=max(maxL,height[i])
                ans+=max(min(maxL,maxR)-height[i],0)
                i+=1
            else:
                maxR=max(maxR,height[j])
                ans+=max(0,min(maxL,maxR)-height[j])
                j-=1
        return ans