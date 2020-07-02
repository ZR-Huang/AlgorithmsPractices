/*
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

示例 1：
输入：nums = [3,4,3,3]
输出：4

示例 2：
输入：nums = [9,1,7,9,7,9,7]
输出：1

限制：
1 <= nums.length <= 10000
1 <= nums[i] < 2^31
*/

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> numCount;
        int res;
        for(auto num : nums){
            if(numCount.count(num)==0) numCount[num] = 1;
            else numCount[num]++;
        }
        for(auto p : numCount){
            if(p.second == 1){
                res = p.first;
                break;
            }
        }
        return res;
    }
    /* 考虑数字的二进制形式，对于出现三次的数字，
    各二进制位 出现的次数都是 3 的倍数。
    因此，统计所有数字的各二进制位中 1 的出现次数，并对 3 求余，
    结果则为只出现一次的数字。*/
    int singleNumber_v2(vector<int>& nums) {
        int count[32] = {0};
        for(int num : nums){
            for(int j = 0; j < 32; j++){
                count[j]+= num & 1;
                num >>= 1;
            }
        }
        int res = 0, m = 3;
        for(int i = 0; i < 32; i++){
            res <<= 1;
            res |= count[31-i] % m;
        }
        return res;
    }

    int singleNumber_v3(vector<int>& nums) {
        int ones=0, twos = 0;
        for(int num : nums){
            ones = ones ^ num & ~twos;
            twos = twos ^ num & ~ones;
        }
        return ones;
    }
};

int main() {
    Solution s ;
    vector<int> nums = {3,4,3,3};
    int res = s.singleNumber_v2(nums);
    cout<< res << endl;
    return 0;
}