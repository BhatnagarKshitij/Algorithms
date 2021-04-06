'''
Question link: https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        returnOutput=list()
        queue=list()
        queue.append(root)
        while queue:
            answer=list()
            queueLength=len(queue)
            while queueLength:
                node=queue.pop(0)
                answer.append(node.val)
                queueLength-=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            returnOutput.append(answer)
        return returnOutput            
            
