#include <iostream>
#include <string>
#include <map>
using namespace std;

typedef pair<string, string> pair;

class Solution {
public:
    /**
     * 两个字符串是否相等
     * @param str1 string字符串 第一个字符串
     * @param str2 string字符串 第二个字符串
     * @return bool布尔型
     */
    map<pair, bool> mem;
    bool isStrsEqu(string str1, string str2) {
        // write code here
        if(mem.find({str1, str2}) != mem.end()) return mem[{str1, str2}];
        int str_len = str1.length();
        if(str_len==1){
            if(str1==str2)
                mem[{str1, str2}] = true;
            else
                mem[{str1, str2}] = false;
            return mem[{str1, str2}];
        }
        string substr11 = str1.substr(0, str_len/2);
        string substr12 = str1.substr(str_len/2, str_len/2);
        string substr21 = str2.substr(0, str_len/2);
        string substr22 = str2.substr(str_len/2, str_len/2);
        if((isStrsEqu(substr11, substr21) && isStrsEqu(substr12, substr22)) || (isStrsEqu(substr11, substr22) && isStrsEqu(substr12, substr21))){
            mem[{str1, str2}] = true;
        }else{
            mem[{str1, str2}] = false;
        }
        return mem[{str1, str2}];
    }
};

int main(){
    cout << Solution().isStrsEqu("abab", "aabb") << endl;
}