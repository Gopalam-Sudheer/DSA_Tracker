class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        goal+=goal
        if s in goal:
            return True
        else:
            return False