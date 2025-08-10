class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def helper(val):
            arr=[0]*10
            temp=0
            while val!=0:
                arr[val%10]+=1
                val//=10
            return ''.join(str(i) for i in arr)
        d=set()
        for i in range(32):
            val=2**i
            d.add(helper(val))
        return helper(n) in d
        
