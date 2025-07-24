class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        k=target
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==k:
                return True
            if nums[low]==nums[mid] and nums[mid]==nums[high]:
                low+=1
                high-=1
            elif nums[low]<=nums[mid]:
                if nums[low]<=k<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=k<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return False