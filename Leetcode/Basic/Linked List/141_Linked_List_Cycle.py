'''
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos 
which represents the position (0-indexed) in the linked list 
where tail connects to. If pos is -1, then there is no cycle 
in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        if not head.next:
            return False
        
        p1 = head
        p2 = head
        while p1 and p2:
            if p2.next and p2.next.next:
                p1 = p1.next
                p2 = p2.next.next
            else:
                return False
            if p1 == p2:
                return True
        
        
        