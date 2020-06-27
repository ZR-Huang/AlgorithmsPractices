/*
注意：本题与主站 3 题相同：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 
提示：
s.length <= 40000
*/
#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // 边缘条件
        if(s.length()==0) return 0;

        int maxLen = 0, curLen = 0;
        int l = 0, r = 0;
        unordered_set<char> charSet;
        while(r < s.length()){
            if(charSet.count(s[r])==0){
                charSet.insert(s[r]);
                curLen++;
                r++;
            } else {
                charSet.erase(s[l]);
                l++;
                curLen--;
            }
            maxLen = max(maxLen, curLen);
        }
        return maxLen;
    }

    int lengthOfLongestSubstring_v2(string s) {
        unordered_map<char, int> last_pos;
        int res = 0, i = -1;
        for (int j = 0; j<s.length(); j++){
            if(last_pos.count(s[j])!=0){
                i = max(last_pos[s[j]], i);
            }
            last_pos[s[j]] = j;
            res = max(res, j-i);
        }
        return res;
    }
};