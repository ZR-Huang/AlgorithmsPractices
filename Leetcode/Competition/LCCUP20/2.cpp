#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int breakfastNumber(vector<int>& staple, vector<int>& drinks, int x) {
        long long ans = 0;
        long long MOD = 1000000007;
        sort(staple.begin(), staple.end());
        sort(drinks.begin(), drinks.end());
        
        int i = 0, j = drinks.size()-1;
        while(i < staple.size() && j >= 0){
            int remain = x - drinks[j];
            while(i < staple.size() && staple[i] <= remain){
                i++;
            }
            ans += i;
            j--;
        }
        if(i >= staple.size() && j >= 0) ans += (j+1)*staple.size();
        
        return ans % MOD;
    }
};

int main(){
    vector<int> staple = {10,20,5};
    vector<int> drinks = {5,5,2};
    cout << Solution().breakfastNumber(staple, drinks, 15) << endl;
    return 0;
}