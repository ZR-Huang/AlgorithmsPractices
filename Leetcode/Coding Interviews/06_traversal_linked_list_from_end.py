'''
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

Example 1:
Input：head = [1,3,2]
Output：[2,3,1]

Constraints:
- 0 <= linkedList.length <= 10000
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        stack.reverse()
        return stack

print(Solution().reversePrint([1,3,2]))