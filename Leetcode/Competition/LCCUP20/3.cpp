#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    int minimumOperations(string leaves) {
        int left = 0, right = leaves.length()-1;
        while(leaves[left] == 'r') left++;
        while(leaves[right]== 'r') right--;
        int r_num = 0, y_num = 0;
        while(left <= right){
            if(leaves[left]=='r') r_num++;
            else y_num++;
            left++;
        }
        return min(r_num, y_num);
    }
};


int main(){
    cout << Solution().minimumOperations("rrryrrrrrryrrr") << endl;
    return 0;
}