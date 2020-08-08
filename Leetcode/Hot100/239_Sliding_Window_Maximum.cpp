#include <deque>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        // 单调队列
        deque<int> q;
        vector<int> answer;
        int l = 0, r = 0;
        while(r < k) {
            while(!q.empty() && nums[r] > q.back()) q.pop_back();
            q.push_back(nums[r]);
            r++;
        }
        while(r < nums.size()) {
            answer.push_back(q.front());
            if(nums[l] == q.front()) q.pop_front();
            l++;
            while(!q.empty() && nums[r] > q.back()) q.pop_back();
            q.push_back(nums[r]);
            r++;
        }
        answer.push_back(q.front());
        return answer;
    }

    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        // 动态规划
        int n = nums.size();
        int left[n], right[n];
        left[0] = nums[0], right[n-1] = nums[n-1];
        for(int i = 1; i<n; i++){
            if(i % k == 0) left[i] = nums[i];
            else left[i] = max(left[i-1], nums[i]);

            int j = n - i - 1;
            if((j+1) % k == 0) right[j] = nums[j];
            else right[j] = max(right[j+1], nums[j]);
        }
        vector<int> answer (n-k+1, 0);
        for(int i = 0; i<n-k+1; i++)
            answer[i] = max(left[i+k-1], right[i]);
        return answer;
    }
};