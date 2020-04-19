/*
Define S = [s,n] as the string S which consists of n connected strings s. 
For example, ["abc", 3] ="abcabcabc".
On the other hand, we define that string s1 can be obtained from string s2 
if we can remove some characters from s2 such that it becomes s1. 
For example, “abc” can be obtained from “abdbec” based on our definition, 
but it can not be obtained from “acbbe”.

You are given two non-empty strings s1 and s2 (each at most 100 characters long) 
and two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. Now consider the strings S1 and S2, 
where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] 
can be obtained from S1.

Example:
Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2
*/
#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>
using namespace std;
class Solution {
public:
    int getMaxRepetitions(string s1, int n1, string s2, int n2) {
        int index=0, s1_cnt = 0, s2_cnt = 0;
        unordered_map<int, pair<int, int>> hash_map;
        pair<int, int> pre_loop, in_loop;
        while(true){
            for (char ch: s1) {
                if (ch == s2[index]) {
                    index++;
                    if (index == s2.size()){
                        s2_cnt++;
                        index = 0;
                    }
                }
            }
            s1_cnt++;
            if (s1_cnt == n1) return s2_cnt / n2;
            if (hash_map.find(index)!=hash_map.end()){
                auto [s1_cnt_prime, s2_cnt_prime] = hash_map[index];
                pre_loop = {s1_cnt_prime, s2_cnt_prime};
                in_loop = {s1_cnt - s1_cnt_prime, s2_cnt - s2_cnt_prime};
                break;
            }
            else hash_map[index] = {s1_cnt, s2_cnt};
        }
        int ans = pre_loop.second + (n1 - pre_loop.first) / in_loop.first * in_loop.second;
        int rest = (n1 - pre_loop.first) % in_loop.first;
        for (int i = 0; i < rest ; i++)
            for (char ch: s1)
                if (ch == s2[index]){
                    index++;
                    if (index == s2.size()) ans++, index=0;
                }
        return ans / n2;
    }
};

int main(){
    string s1 = "acb", s2 = "ab";
    int n1 = 4, n2 = 2;
    Solution s ;
    int M = s.getMaxRepetitions(s1, n1, s2, n2);
    return 0;
}
