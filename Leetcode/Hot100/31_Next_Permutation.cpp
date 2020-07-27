/*
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
*/
#include <vector>
using namespace std;


class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i = nums.size()-2;
        int j = nums.size()-1;
        // 从右往左找到第一个nums[i] < nums[i+1]
        while (i >= 0 && nums[i+1] <= nums[i]){
            i--;
        }
        if(i >= 0){ // 不是最后一个排列
            // 从右往左找到第一个大于nums[i]的元素
            while (j >= i && nums[j] <= nums[i]){
                j--;
            }
            swap(nums, i, j);
        }
        // 将nums[i]之后的元素重新调整为升序
        for(i = i+1, j = nums.size()-1; i<j; i++, j--){
            swap(nums, i, j);
        }
    }

    void swap(vector<int>& nums, int i, int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
};