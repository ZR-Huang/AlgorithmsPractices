#include <iostream>
#include <string>
#include <map>
using namespace std;

class Solution {
public:
    /**
     * 获取满足条件的最长子串的长度
     * @param str string字符串 输入的字符串
     * @return int整型
     */
    int getMaxSubstringLen(string str) {
        // write code here
        int ans = 0;
        for(int i =0; i<str.length(); i++){
            map<char, int> count;
            count['a'] = 0, count['b'] = 0, count['c'] = 0, count['d'] = 0, count['e'] = 0;
            for(int j = i; j<str.length(); j++){
                if(count.find(str[j])!=count.end()) count[str[j]]++;
                if(check(count)) {
                    ans = max(ans, j-i+1);
                }
            }
        }
        return ans;
    }

    bool check(map<char, int> count){
        for(auto p: count){
            if(p.second % 2 ==1) return false;
        }
        return true;
    }
};

int main() {
    cout << Solution().getMaxSubstringLen("aabbffced") << endl;
    return 0;
}