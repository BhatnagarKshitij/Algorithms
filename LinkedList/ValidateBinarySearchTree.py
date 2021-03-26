'''
Question link: https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        output=[]
        def inNode(root,output):
            if root:
                if root.left:
                    inNode(root.left,output)
                output.append(root.val)
                if root.right:
                    inNode(root.right,output)
        inNode(root,output)
        outputOne=output
        output=sorted(set(output))
        if output==outputOne:
            return True
        else:
            return False
        
        
