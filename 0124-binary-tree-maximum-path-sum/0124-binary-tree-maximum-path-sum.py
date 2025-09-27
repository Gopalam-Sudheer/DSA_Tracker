# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root is None:
                return 0
            left=max(0,helper(root.left))
            right=max(0,helper(root.right))
            self.ans=max(self.ans,root.val+left+right)
            return root.val+max(left,right)
        self.ans=float('-inf')
        helper(root)
        return self.ans