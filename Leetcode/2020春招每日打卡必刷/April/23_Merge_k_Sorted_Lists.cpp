/*
Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
*/
#include <iostream>
#include <vector>
using namespace std;
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.empty()) return NULL;
        if(lists.size()==1) return lists[0];
        for(int i=1; i<lists.size(); i++){
            lists[i] = mergeTwoLists(lists[i-1], lists[i]);
        }
        return lists[lists.size()-1];
    }
    
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2){
        ListNode* cur;
        ListNode* dum;
        dum = new ListNode(0);
        cur = dum;
        while(l1!=NULL && l2!=NULL){
            if(l1->val < l2->val){
                cur->next = l1;
                l1 = l1->next;
            }
            else{
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }
        cur->next = l1 ? l1 : l2;
        return dum->next;
    }
};