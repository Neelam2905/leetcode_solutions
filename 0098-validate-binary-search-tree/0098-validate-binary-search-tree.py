# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev=None
        self.isValid=True
        self.inOrder(root)
        return self.isValid
    def inOrder(self,curr):
        if curr is None:
            return
        self.inOrder(curr.left)
        if self.prev is not None and self.prev>curr.val:
            self.isValid=False
            return 
        self.prev=curr.val
        self.inOrder(curr.right)