/*
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:
s = "abaccdeff"
返回 "b"

s = "" 
返回 " "
 
限制：
0 <= s 的长度 <= 50000
*/
#include <string>
#include <unordered_map>
#include <map>
using namespace std;

class Solution {
public:
    char firstUniqChar(string s) {
        unordered_map<char, int> charCount;
        for(auto c : s){
            if(charCount.count(c)==0){
                charCount[c] = 1;
            } else {
                charCount[c]++;
            }
        }
        for(auto c : s){
            if(charCount[c]==1){
                return c;
            }
        }
        return ' ';
    }
};