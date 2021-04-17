'''
Question link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None: return None
        
        temp = head
        
        while temp.next != None:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
#        data=dict()
#        root=ListNode()
#        temp=root
#        while(head):
#            if data.get(head.val,False) is False:
#                data[head.val]=1
#                temp.next=ListNode(head.val)
#                temp=temp.next
#            head=head.next
#        return root.next
        
