#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#define MOD 1000000007
using namespace std;

int dfs(int depth, int prev_level_node, int index, vector<int>& dep_vec){
    if(index >= dep_vec.size()) return 1;
    long long total_pos = pow(2, prev_level_node);
    long long curr_num = 0;
    for(int i = index; dep_vec[i]==depth; i++) curr_num++;
    if(curr_num==0 || curr_num > 2* prev_level_node) return 0; // 主要是忘了这个判断
    long long a=1, b=1;
    for(int i = total_pos; i>=total_pos-curr_num+1; i--) a*=i;
    for(int i = curr_num; i>0; i--) b*=i;
    int res = (a / b) % MOD;
    return res * dfs(depth+1, curr_num, index+curr_num, dep_vec);
}

int main(){
    int N;
    cin >> N;
    vector<int> dep_vec (N, 0);
    for(int i = 0; i<N;i++)
        cin >> dep_vec[i];
    sort(dep_vec.begin(), dep_vec.end());
    cout<< dfs(0, 0, 0, dep_vec);
    return 0;
}