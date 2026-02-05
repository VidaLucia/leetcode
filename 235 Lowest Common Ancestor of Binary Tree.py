# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # traverse left and right, check for when root.val = p or root.val = q return as l,r
        # travel down and we find p or q -> we return p or q up one layer if not we return None
        # then we look with an if statement if p = root.left and q = root.right and if they are not none, if they are equal we return the node value

        if not root:
            return None
    
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left if left else right