'''
Question link: https://leetcode.com/problems/reverse-linked-list-ii/

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#CodeWithKshitij
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left==right:
            return head

        leftPtr=head
        rightPtr=head
        values=[]
        
        while right!=0:
            if left-1:
                leftPtr=leftPtr.next
                left-=1
            else:
                values.append(rightPtr.val)
            rightPtr=rightPtr.next
            right-=1
        
        while values:
            leftPtr.val=values.pop()
            leftPtr=leftPtr.next
        return head
