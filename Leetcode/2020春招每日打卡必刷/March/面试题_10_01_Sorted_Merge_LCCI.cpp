/*
You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. 
Write a method to merge B into A in sorted order.

Initially the number of elements in A and B are m and n respectively.

Example:
Input:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
*/
#include <vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& A, int m, vector<int>& B, int n) {
        int i = m-1, j=n-1, k = m+n-1;
        while (i >= 0 and j >= 0)
        {
            if(A[i]>=B[j]) A[k--]=A[i--];
            else A[k--]=B[j--];
        }
        while (j>=0) A[k--]=B[j--];
    }
};