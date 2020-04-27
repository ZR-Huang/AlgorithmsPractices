/*
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

限制：
1 <= s 的长度 <= 8
*/
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<string> ans;
    vector<string> permutation(string s) {
        if (s.empty()) return ans;
        unordered_map<char, int> count = get_vocabulary(s);
        backtrack(s, count, "");
        return ans;
    }
    unordered_map<char, int> get_vocabulary(string s) {
        unordered_map<char, int> count;
        for (auto c: s){
            if (count.find(c)==count.end())
                count.insert({c, 1});
            else
                count.find(c)->second++;
        } 
        return count;
    }
    void backtrack(string s, unordered_map<char, int>& count, string prefix) {
        if(prefix.length() == s.length()) ans.push_back(prefix);
        for (auto & iter: count){
            // unordered_map<char, int>::iterator iter = count.find(c);
            if(iter.second!=0){
                iter.second--;
                // char c = iter.first;
                backtrack(s, count, prefix+iter.first);
                iter.second++;
            }
        }
    }
};

int main(){
    Solution s;
    vector<string> ans = s.permutation("abc");
    return 0;
}