# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=0
    def helper(self,root,maxi):
        if root is None:
            return 
        if root.val>=maxi:
            self.ans+=1
        self.helper(root.left,max(maxi,root.val))
        self.helper(root.right,max(maxi,root.val))
    def goodNodes(self, root: TreeNode) -> int:
        self.helper(root,root.val)
        return self.ans