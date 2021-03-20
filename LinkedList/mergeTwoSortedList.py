'''
Question link: https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return
        elif not l1:
            return l2
        elif not l2:
            return l1
        
        sortedListNode=ListNode()
        head=sortedListNode
        while l1 and l2:
            if l1.val<l2.val:
                sortedListNode.next=ListNode(l1.val)
                l1=l1.next
            else:
                sortedListNode.next=ListNode(l2.val)
                l2=l2.next
            sortedListNode=sortedListNode.next
        
        while l1:
            sortedListNode.next=ListNode(l1.val)
            sortedListNode=sortedListNode.next
            l1=l1.next
        
        while l2:
            sortedListNode.next=ListNode(l2.val)
            sortedListNode=sortedListNode.next
            l2=l2.next
            
        
        return head.next