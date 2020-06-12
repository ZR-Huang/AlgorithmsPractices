/*
Implement a method to perform basic string compression using the counts 
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. 
If the "compressed" string would not become smaller than the original string, 
your method should return the original string. You can assume the string has 
only uppercase and lowercase letters (a - z).

Example 1:
Input: "aabcccccaaa"
Output: "a2b1c5a3"

Example 2:
Input: "abbccd"
Output: "abbccd"
Explanation: 
The compressed string is "a1b2c2d1", which is longer than the original string.
 
Note:
0 <= S.length <= 50000
*/
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string compressString(string S) {
        string compress_str;
        int i = 0, j = 0;
        while(j < S.size()){
            if(S[i]==S[j]) j++;
            else{
                compress_str += S[i] + to_string(j-i);
                i = j;
            }
        }
        compress_str += S[i] + to_string(j-i);
        return compress_str.size() < S.size() ? compress_str : S;   
    }
};

int main() {
    Solution *s = new Solution();
    string res = s->compressString("aaccDDbbAAAccaa");
    cout << res << endl;
    return 0;
}