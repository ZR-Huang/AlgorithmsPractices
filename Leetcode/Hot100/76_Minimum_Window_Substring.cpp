#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;

class Solution {
public:
    unordered_map<char, int> need, window;
    string minWindow(string s, string t) {
        for (char c : t) need[c]++;
        int left = 0, right = 0;
        int valid = 0;
        int start = 0, minLen = INT_MAX;
        while(right < s.size()){
            char c = s[right];
            right++;
            if (need.count(c)) {
                window[c]++;
                if(window[c]==need[c])
                    valid++;
            }
            // 判断左窗口是否要收缩
            while(valid == need.size()){
                if (right - left < minLen){
                    start = left;
                    minLen = right - left;
                }
                char d = s[left];
                left++;
                if(need.count(d)){
                    window[d]--;
                    if(window[d]<need[d])
                        valid--;
                }
            }
        }
        return minLen == INT_MAX ? "" : s.substr(start, minLen);
    }
};