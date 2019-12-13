'''
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # reverse the linked list iteratively
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next

        if len(values) == 1:
            return head

        node = head
        for i in range(len(values)-1, -1, -1):
            node.val = values[i]
            node = node.next
        
        return head

    
    def reverseList_2(self, head):
        # reverse the linked list using two pointers
        if not head or not head.next:
            return head
        
        rev_head = None
        while head:
            temp = head
            head = head.next
            temp.next = rev_head
            rev_head = temp
        
        return rev_head


    def reverseList_3(self, head):
        # do it recursively
        def reverse(head):
            if not head or not head.next:
                return head, head
            
            rev_head, tail = reverse(head.next)
            tail.next = head
            tail = tail.next

            return rev_head, tail

        rev_head, tail = reverse(head)
        if tail:
            tail.next = None
        return rev_head
