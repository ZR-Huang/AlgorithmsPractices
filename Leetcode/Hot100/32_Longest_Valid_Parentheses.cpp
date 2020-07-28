/*
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
*/
#include <string>
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        // Dynamic programming
        int length = s.length(), ans = 0;
        if (length < 2)
            return 0;
        vector<int> dp(length, 0);
        for (int i=1; i < length; i++) {
            if(s[i] == ')'){
                if(s[i-1] == '(')
                    dp[i] = (i >= 2 ? dp[i-2] : 0) + 2;
                else if (i-dp[i-1]>=1 && s[i-dp[i-1]-1]=='(')
                    dp[i] = dp[i-1] + (i-dp[i-1]>=2 ? dp[i-dp[i-1]-2] : 0) + 2;
                ans = max(ans, dp[i]);
            }
        }
        return ans;
    }

    int useStack(string s) {
        // Stack
        int length = s.length(), ans = 0;
        if (length < 2)
            return 0;
        stack<int> stackOfIndex;
        stackOfIndex.push(-1);
        for(int i = 0; i < length; i++) {
            if(s[i] == '(') stackOfIndex.push(i);
            else {
                stackOfIndex.pop();
                if (stackOfIndex.empty())
                    stackOfIndex.push(i);
                else 
                    ans = max(ans, i - stackOfIndex.top());
            }
        }
        return ans;
    }

    int twoPointer(string s) {
        int left = 0, right = 0, ans = 0;
        for (int i = 0; i < s.length(); i++){
            if(s[i]=='(') left++;
            else right++;
            if(left==right) ans = max(ans, (left+right));
            if(right>left) left = right = 0;
        }
        left = right = 0;
        for (int i = s.length()-1; i >= 0; i--) {
            if(s[i]=='(') left++;
            else right++;
            if(left==right) ans = max(ans, (left+right));
            if(left > right) left = right = 0;
        }
        return ans;
    }
};