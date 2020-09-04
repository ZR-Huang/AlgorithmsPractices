#include <iostream>
#include <set>
#include <vector>
using namespace std;

int ans = 10000000;
set<pair<int, int>> visited;
void dfs(vector<vector<int>> &board, int x, int y, int sum, int N){
    if(x == N-1 && y==N-1){
        ans = min(ans, sum);
        return;
    }
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};
    for (int i=0; i<4; i++){
        if(visited.count({x+dx[i], y+dy[i]})!=0) continue;
        if(x + dx[i] >=0 && x + dx[i] < N && y + dy[i]>=0 && y+dy[i]<N){
            visited.insert({x+dx[i], y+dy[i]});
            sum += abs(board[x][y]-board[x+dx[i]][y+dy[i]]);
            dfs(board, x+dx[i], y+dy[i], sum, N);
            visited.erase({x+dx[i], y+dy[i]});
        }
    }
}

int main(){
    // int N;
    // cin >> N;
    // vector<vector<int>> board(N, vector<int>(N, 0));
    // for(int i = 0; i<N; i++){
    //     for (int j=0; j<N; j++){
    //         cin >> board[i][j];
    //     }
    // }
    int N = 3;
    vector<vector<int>> board ({{1,2,4}, {1,3,1}, {1,2,1}});
    dfs(board, 0, 0, 0, N);
    cout << ans;
    return 0;
}