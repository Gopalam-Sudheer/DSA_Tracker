class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin=0
        leftMax=0
        for i in s:
            if i=='(':
                leftMin,leftMax=leftMin+1,leftMax+1
            elif i==')':
                leftMin,leftMax=leftMin-1,leftMax-1
            else:
                leftMin,leftMax=leftMin-1,leftMax+1
            if leftMax<0:
                return False
            leftMin=max(0,leftMin)
        return leftMin==0