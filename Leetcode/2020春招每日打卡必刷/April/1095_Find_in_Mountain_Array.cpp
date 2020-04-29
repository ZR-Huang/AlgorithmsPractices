/*
(This problem is an interactive problem.)

You may recall that an array A is a mountain array if and only if:
    A.length >= 3
    There exists some i with 0 < i < A.length - 1 such that:
        A[0] < A[1] < ... A[i-1] < A[i]
        A[i] > A[i+1] > ... > A[A.length - 1]

Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  
If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:
    MountainArray.get(k) returns the element of the array at index k (0-indexed).
    MountainArray.length() returns the length of the array.

Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  
Also, any solutions that attempt to circumvent the judge will result in disqualification.

Example 1:
Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Example 2:
Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.

Constraints:
    3 <= mountain_arr.length() <= 10000
    0 <= target <= 10^9
    0 <= mountain_arr.get(index) <= 10^9
*/

#include <iostream>
using namespace std;

// This is the MountainArray's API interface.
// You should not implement it, or speculate about its implementation
class MountainArray {
  public:
    int get(int index);
    int length();
};


class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int peak = findPeak(mountainArr);
        int ans = left_binary_search(target, mountainArr, 0, peak);
        if(ans == -1) ans = right_binary_search(target, mountainArr, peak, mountainArr.length()-1);
        return ans;
    }
    int findPeak(MountainArray &mountainArr){
        int left=0, right=mountainArr.length()-1;
        while(left < right){
            int mid = (left+right) / 2;
            int mid_value = mountainArr.get(mid);
            int mid_left_value = mountainArr.get(mid-1);
            int mid_right_value = mountainArr.get(mid+1);
            if(mid_left_value < mid_value && mid_value < mid_right_value)
                left = mid ;
            else if (mid_left_value > mid_value && mid_value > mid_right_value)
                right = mid ;
            else if (mid_left_value < mid_value && mid_value > mid_right_value)
                return mid;
        }
        return -1;
    }
    int left_binary_search(int target, MountainArray &mountainArr, int left, int right){
        while(left <= right){
            int mid = (left+right) / 2;
            int mid_val = mountainArr.get(mid);
            if(mid_val < target)
                left = mid + 1;
            else if(mid_val > target)
                right = mid -1;
            else
                return mid;
        }
        return -1;
    }
    int right_binary_search(int target, MountainArray &mountainArr, int left, int right){
        while(left <= right){
            int mid = (left+right) / 2;
            int mid_val = mountainArr.get(mid);
            if(mid_val < target)
                right = mid-1;
            else if(mid_val > target)
                left = mid+1;
            else
                return mid;
        }
        return -1;
    }
};