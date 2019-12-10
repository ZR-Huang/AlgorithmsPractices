'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # do this by traversing the linked list twice
        # Step 1. Get the length of the linked list
        # Step 2. Remove the node
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        if length == 1:
            return None
        if length - n == 0:
            head = head.next
            return head
        
        node = head
        for _ in range(length-n-1):
            node = node.next
        node.next = node.next.next

        return head
