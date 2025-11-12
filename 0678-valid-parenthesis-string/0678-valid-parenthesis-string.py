class Solution:
    def checkValidString(self, s: str) -> bool:
        mi=0
        ma=0
        for i in s:
            if i=='(':
                mi+=1
                ma+=1
            elif i==')':
                mi-=1
                ma-=1
            else:
                mi-=1
                ma+=1
            if ma<0:
                return False
            mi=max(mi,0)
        return mi==0