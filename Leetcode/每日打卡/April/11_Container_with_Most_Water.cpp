/*
Given n non-negative integers a1, a2, ..., an , where each represents a point at 
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of 
line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution{
    public:
    int maxArea(vector<int>& height){
        int max_area = 0;
        for (int i=0; i < height.size()-1; i++) {
            for (int j=i+1; j < height.size(); j++) {
                int area = (j-i) * min(height[i], height[j]);
                max_area = max(max_area, area);
            }
        }
        return max_area;
    }

    int maxArea(vector<int>& height){
        int left = 0, right = height.size()-1;
        int max_area = (right-left)*min(height[left], height[right]);
        while (left<right){
            if (height[left]<height[right]) left++;
            else right--;
            int area = (right-left)*min(height[left], height[right]);
            max_area = max(max_area, area);
        }
        return max_area;
    }
};