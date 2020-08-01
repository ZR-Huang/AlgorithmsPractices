/*
Given a linked list and a value x, partition it such that all nodes less than x come 
before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
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
    ListNode* partition(ListNode* head, int x) {
        if (!head || !head->next) return head;
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode *left, *right;
        left = dummy;
        while(left->next && left->next->val < x) left = left->next;
        ListNode *pre;
        pre = left, right = left->next;
        while(right){
            if(right->val<x){
                // 交换结点
                pre->next = right->next;
                right->next = left->next;
                left->next = right;
                right = pre->next;
                left = left->next;
            } else {
                right = right->next;
                pre = pre->next;
            }
        }
        return dummy->next;
    }
};