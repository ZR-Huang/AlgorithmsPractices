'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l2 if not l1 else l1
        if not l1 and not l2:
            return None
        
        new_list = None
        if l1.val <= l2.val:
            new_list = l1
            l1 = l1.next
        else:
            new_list = l2
            l2 = l2.next
        head = new_list
        while l1 and l2:
            if l1.val <= l2.val:
                new_list.next = l1
                l1 = l1.next
            else:
                new_list.next = l2
                l2 = l2.next
            new_list = new_list.next
        
        new_list.next = l1 if l1 else l2

        return head
