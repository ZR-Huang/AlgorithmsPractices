/*
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
*/
#include <string>
using namespace std;

class Solution {
public:
    string decodeString(string s) {
        int i = 0;
        while(i < s.length() && !isdigit(s[i])){
            i++;
        }
        if(i==s.length()) return s;
        string prefix = s.substr(0, i);
        int digit_start = i;
        while(i < s.length() && isdigit(s[i])){
            i++;
        }
        int k = stoi(s.substr(digit_start, i-digit_start));
        int left = 0;
        int mid_start = i;
        while(i < s.length()){
            if(s[i]=='[') left++;
            else if(s[i]==']') left--;
            if(left==0) break;
            i++;
        } 
        int mid_end = i;
        // string suffix = i == s.length()-1 ? "" : s.substr(i+1, s.length()-i-1);
        string mid = decodeString(s.substr(mid_start+1, mid_end-mid_start-1));
        string complt_mid = "";
        while(k--){
            complt_mid += mid;
        }
        string suffix = decodeString(s.substr(i+1, s.length()-i-1));
        return prefix + complt_mid + suffix;
    }
};

int main(){
    string ans = Solution().decodeString("abc3[cd]xyz");
    return 0;
}