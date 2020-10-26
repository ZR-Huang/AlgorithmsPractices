/*
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
*/

#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0, right = 0, max_len = 0;
        unordered_set<char> visited;
        while (right < s.size())
        {
            if(visited.find(s[right]) == visited.end()){
                visited.insert(s[right]);
                max_len = max(max_len, right-left+1);
                right++;
            } else {
                visited.erase(s[left]);
                left++;
            }
        }
        return max_len;
    }
};

int main(){
    Solution s;
    s.lengthOfLongestSubstring("abcabcbb");
    return 0;
}