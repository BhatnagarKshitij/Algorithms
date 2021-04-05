'''
Question link: https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def isSymmetric(self, root):
        return self.isMirror(root,root)
        
    def isMirror(self,leftTree,rightTree):
        if leftTree==None and rightTree==None:
            return True 
        
        if leftTree==None or rightTree==None:
            return False
        
        return (leftTree.val==rightTree.val) and self.isMirror(leftTree.right,rightTree.left) and self.isMirror(leftTree.left,rightTree.right)
