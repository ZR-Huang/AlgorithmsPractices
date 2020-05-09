/*
Implement int sqrt(int x).
Compute and return the square root of x, 
where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and 
only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
*/
#include <iostream>
using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        if(x == 0 ) return 0;
        int res = 1;
        while (res <= x/res)
        {
            res++;
        }
        return --res;
    }

    int mySqrt(int x) {
        if(x == 0) return 0;
        int l = 1, r = x/2;
        while (l <= r)
        {
            int mid = l + (r - l) / 2;
            if(mid == x / mid) return mid;
            else if (mid < x/mid) l = mid+1;
            else r = mid - 1;
        }
        return r;
    }
};