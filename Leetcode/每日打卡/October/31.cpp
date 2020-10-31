
#include <unordered_map>
#include <set>
#include <vector>
using namespace std;

class RandomizedCollection {
public:
    unordered_map<int, set<int>> ids;
    vector<int> num;
    /** Initialize your data structure here. */
    RandomizedCollection() {

    }
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    bool insert(int val) {
        num.push_back(val);
        ids[val].insert(num.size()-1);
        return ids[val].size() == 1;
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    bool remove(int val) {
        if (ids.find(val) == ids.end()){
            return false;
        }
        int i = *(ids[val].begin());
        num[i] = num.back();
        ids[val].erase(i);
        ids[num[i]].erase(num.size()-1);
        if( i < num.size() - 1){
            ids[num[i]].insert(i);
        }
        if( ids[val].size() == 0){
            ids.erase(val);
        }
        num.pop_back();
        return true;
    }
    
    /** Get a random element from the collection. */
    int getRandom() {
        return num[rand() % num.size()];
    }
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection* obj = new RandomizedCollection();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */