class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def insert(result,occ,num):
            if occ[num]>0:
                internal_remove(result,(occ[num],num))
            occ[num]+=1
            internal_insert(result,(occ[num],num))
        def remove(result,occ,num):
            internal_remove(result,(occ[num],num))
            occ[num]-=1
            if occ[num]>0:
                internal_insert(result,(occ[num],num))
        def internal_insert(result,p):
            if len(large)<x or p>large[0]:
                result[0]+=p[0]*p[1]
                large.add(p)
                if len(large)>x:
                    to_remove=large[0]
                    result[0]-=to_remove[0]*to_remove[1]
                    large.remove(to_remove)
                    small.add(to_remove)
            else:
                small.add(p)
        def internal_remove(result,p):
            if p>=large[0]:
                result[0]-=p[0]*p[1]
                large.remove(p)
                if small:
                    to_add=small[-1]
                    result[0]+=to_add[0]*to_add[1]
                    small.remove(to_add)
                    large.add(to_add)
            else:
                small.remove(p)
        large=SortedList()
        small=SortedList()
        occ=defaultdict(int)
        result=[0]
        ans=[]
        for i in range(len(nums)):
            insert(result,occ,nums[i])
            if i>=k:
                remove(result,occ,nums[i-k])
            if i>=k-1:
                ans.append(result[0])
        return ans
