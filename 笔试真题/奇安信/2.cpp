#include <unordered_map>
#include <iostream>
using namespace std;

class Solution {
public:
    /**
     * 
     * @param num_money int整型 奖金的总数,单位为元
     * @return int整型
     */
    int CalulateMethodCount(int num_money) {
        // write code here
        unordered_map<int, int> mem;
        mem[0] = 1, mem[1] = 1;
        return dfs(num_money, mem);
    }
    
    int dfs(int n, unordered_map<int, int>& mem){
        if(mem.find(n) != mem.end()) return mem[n];
        int res = 0;
        for(int i=1; i<=n; i++){
            res += dfs(n-i, mem);
        }
        mem[n] = res;
        return mem[n];
    }
};

int main (){
    cout << Solution().CalulateMethodCount(3) << endl;
    return 0;
}