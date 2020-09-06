/*
安全技术方向
Leetcode 3
剑指offer 48原题
最长不含重复字符的子字符串
*/
#include <unordered_set>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
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
};