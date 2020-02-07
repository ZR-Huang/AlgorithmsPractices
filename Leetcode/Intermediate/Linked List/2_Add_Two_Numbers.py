'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = [0]

        def add(l1, l2, carry):
            _sum = carry[0] + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry[0] = _sum // 10
            return ListNode(_sum % 10)
        
        ans_head = add(l1, l2, carry)
        curr_node = ans_head
        l1 = l1.next
        l2 = l2.next
        while l1 or l2:
            curr_node.next = add(l1, l2, carry)
            curr_node = curr_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry[0] != 0:
            curr_node.next = ListNode(carry[0])
        
        return ans_head
            
            
