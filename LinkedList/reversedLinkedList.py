'''
Question link: https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        elif not  head.next:
            return head
            
        pointer1=head
        head=head.next
        pointer1.next=None
        while head.next:
            pointer2=head.next
            head.next=pointer1
            pointer1=head
            head=pointer2
        else:
            head.next=pointer1
            pointer1=head
            
        return pointer1
        