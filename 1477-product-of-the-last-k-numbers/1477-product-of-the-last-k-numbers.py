class ProductOfNumbers:
    
    def __init__(self):
        self.arr=[]

    def add(self, num: int) -> None:
        if num==0:
            self.arr=[]
        elif len(self.arr)==0:
            self.arr.append(num)
        else:
            self.arr.append(self.arr[-1]*num)

    def getProduct(self, k: int) -> int:
        if len(self.arr)<k:
            return 0
        elif len(self.arr)==k:
            return self.arr[-1]
        else:
            return self.arr[-1]//self.arr[-1-1*k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)