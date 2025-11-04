class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]
        for i in asteroids:
            if len(ans)==0 or i>0:
                ans.append(i)
                continue
            while ans and ans[-1]>0 and ans[-1]<abs(i):
                ans.pop()
            if ans and ans[-1]==abs(i):
                ans.pop()
            elif ans and ans[-1]>abs(i):
                continue
            else:
                ans.append(i)
        return ans