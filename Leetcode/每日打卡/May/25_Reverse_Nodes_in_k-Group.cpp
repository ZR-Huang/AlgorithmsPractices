/*
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
*/

#include <iostream>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head == NULL || head->next == NULL) return head;
        ListNode *left = head, *right = head, *new_head, *last_end = NULL;
        int count = 0;
        while (left != NULL && right != NULL)
        {
            int i;
            for (i = 0; i < k && right != NULL; i++)
                right = right->next;
            if (i == k){
                ListNode *res = reverseLinkedList(left, right);
                if (count == 0) new_head = res;
                else last_end->next = res;
                count++;
                last_end = left;
                left = right;
            }
            else break;
        }
        return new_head;
    }

    ListNode* reverseLinkedList(ListNode* head, ListNode* next_head) {
        if (head->next == NULL) return head;
        ListNode *last = next_head, *p1 = head, *p2 = head->next;
        while (p2!=next_head)
        {
            p1->next = last;
            last = p1;
            p1 = p2;
            p2 = p2->next;
        }
        p1->next = last;
        return p1;
    }
};

int main() {
    ListNode *head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);
    Solution s;
    s.reverseKGroup(head, 2);
    return 0;
}