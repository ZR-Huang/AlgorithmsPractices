/*
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
*/

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool find = false;
    bool wordBreak(string s, vector<string>& wordDict) {
        // LTE
        dfs(s, 0, s.length()-1, wordDict);
        return find;
    }

    void dfs(string s, int start, int end, vector<string>& wordDict) {
        if(start > end){
            find = true;
        }
        for(string word : wordDict){
            if(find) break;
            int wordLen = word.length();
            bool match = true;
            if(start + wordLen - 1 <= end){
                for (int i = 0 ; i < wordLen; i++ ){
                    if(s[start+i] != word[i]){
                        match = false;
                        break;
                    }
                }
                if(match) dfs(s, start+wordLen, end, wordDict);
            }
        }
    }

    bool dp(string s, vector<string>& wordDict) {
        vector<bool> dp(s.length()+1, false);
        dp[0] = true;
        for (int i = 1; i<=s.length(); i++) {
            for (string word : wordDict){
                int len = word.length();
                if(i-len >= 0 && dp[i-len]){
                    dp[i] = (dp[i] || compareStr(s, i-len, s.length(), word));
                }
            }
        }
        return dp[s.length()];
    }

    bool compareStr(string s, int start, int end, string word) {
        for (int i = 0; i<word.length(); i++) {
            if (s[start+i]!=word[i]) return false;
        }
        return true;
    }
};