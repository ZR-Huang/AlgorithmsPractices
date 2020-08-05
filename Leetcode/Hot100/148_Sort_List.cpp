/*
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
*/

#include <iostream>
using namespace std;

//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* sortList(ListNode* head) {
        // get the length of linked list
        int length = 0;
        ListNode *curr = head;
        while(curr) {
            length++;
            curr = curr->next;
        }
        if(length==0 || length == 1) return head;
        int half_length = length / 2;
        ListNode *left, *right, *prev;
        left = right = head;
        while(half_length){
            prev = right;
            right = right->next;
            if(half_length==1) prev->next = NULL;
            half_length--;
        }
        left = sortList(left);
        right = sortList(right);
        left = merge(left, right);
        return left;
    }

    ListNode *merge(ListNode *left, ListNode *right) {
        ListNode *head = new ListNode(0), *curr;
        curr = head;
        while(left && right){
            if (left->val < right->val){
                curr->next = left;
                left = left->next;
            } else {
                curr->next = right;
                right = right->next;
            }
            curr = curr->next;
        }
        curr->next = left ? left : right;
        return head->next;
    }
};