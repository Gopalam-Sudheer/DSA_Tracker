class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        f=-1
        l=-1
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                f=mid
                end=mid-1
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                l=mid
                start=mid+1
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return [f,l]
