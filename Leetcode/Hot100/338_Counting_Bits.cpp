/*
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:
Input: 2
Output: [0,1,1]

Example 2:
Input: 5
Output: [0,1,1,2,1,2]

Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
*/
#include <vector>
#include <math.h>
using namespace std;

class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> ans(num+1, 0);
        ans[0] = 0;
        if(num==0) return ans;
        ans[1] = 1;
        if(num==1) return ans;
        for(int i=1; ;i++){
            int start = pow(2, i);
            int end = pow(2, i+1);
            for(int j=start; j<end; j++){
                ans[j] = ans[j-start] + 1;
                if(j == num) return ans;
            }
        }
    }

    vector<int> countBits(int num) {
        vector<int> ans(num+1, 0);
        if(num == 0) return ans;
        for(int i = 1; i <= num; i++){
            if(i & 1 == 1) ans[i] = ans[i-1]+1;
            else ans[i] = ans[i/2];
        }
        return ans;
    }
};