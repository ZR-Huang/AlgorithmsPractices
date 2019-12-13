'''
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        Find the middle of the linked list and reverse the half of the 
        linked list.
        - Two pointers
        '''
        if not head or not head.next:
            return True
        else:
            slow = head
            quick = head
        
        rev_head = None
        while quick and quick.next:
            # move forward pointers and reverse the linked list
            temp = slow
            slow = slow.next
            quick = quick.next.next
            temp.next = rev_head
            rev_head = temp

        if not quick: # the length of the linked list is even
            quick = slow
        else:
            quick = slow.next
        
        while quick and rev_head:
            if quick.val != rev_head.val:
                return False
            quick = quick.next
            rev_head = rev_head.next
        
        return True
            
