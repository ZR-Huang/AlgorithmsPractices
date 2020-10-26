'''
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed. 

Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        count = 0
        while head:
            count += 1
            head = head.next
        head = l2
        while head:
            count -= 1
            head = head.next        
        if count <0:
            l1, l2 = l2, l1
        last = head = ListNode(0)
        head.next = l1
        for _ in range(abs(count)):
            if l1.val != 9:
                last = l1
            l1 = l1.next
        while l1:
            temp = l1.val + l2.val
            if temp > 9:
                temp -= 10
                last.val += 1
                last = last.next
                while last != l1:
                    last.val = 0 
                    last = last.next
            elif temp != 9:
                last = l1
            l1.val = temp
            l1 = l1.next
            l2 = l2.next
        return head if head.val == 1 else head.next

l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(Solution().addTwoNumbers(l1, l2))