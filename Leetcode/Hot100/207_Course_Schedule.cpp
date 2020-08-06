/*
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses? 

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

Constraints:
- The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
- You may assume that there are no duplicate edges in the input prerequisites.
- 1 <= numCourses <= 10^5
*/

#include <unordered_set>
#include <unordered_map>
#include <vector>

using namespace std;

struct Node {
    int course;
    Node *next;
    Node(int x): course(x), next(NULL) {}
};

class Solution {
public:
    bool isCycle = false;
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // LTE
        unordered_map<int, Node*> graph = createGraph(prerequisites);
        for(int i=0; i<numCourses; i++) {
            unordered_set<int> visited;
            visited.insert(i);
            if(!isCycle) dfs(i, graph, visited);
            else return false;
        }
        return true;
    }

    unordered_map<int, Node*> createGraph(vector<vector<int>>& prerequisites) {
        unordered_map<int, Node*> graph;
        for(vector<int> pair : prerequisites) {
            if(graph.count(pair[1])==0) {
                graph[pair[1]] = new Node(pair[0]);
            } else {
                Node *tail = graph[pair[1]];
                while(tail->next) tail = tail->next;
                tail->next = new Node(pair[0]);
            }
        }
        return graph;
    }

    void dfs(int course, unordered_map<int, Node*>& graph, unordered_set<int>& visited) {
        if (graph.count(course)==0) return;
        Node *curr = graph[course];
        while(curr) {
            if(visited.count(curr->course)==0 && !isCycle) {
                visited.insert(curr->course);
                dfs(curr->course, graph, visited);
                visited.erase(curr->course);
            } else {
                isCycle = true;
                break;
            }
            curr = curr->next;
        }
    }
    // 以下方法为题解，拓扑排序+dfs
    vector<vector<int>> edges;
    vector<int> visited; // visited[i]==0 -- 未搜索，visited[i]==1 -- 搜索中，visited[i]==2 -- 已完成
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        edges.resize(numCourses);
        visited.resize(numCourses);
        for(vector<int> pair : prerequisites)
            edges[pair[1]].push_back(pair[0]);
        for(int i = 0; i<numCourses && !isCycle; i++){
            if(!visited[i]){
                dfs(i);
            }
        }
        return isCycle;
    }
    void dfs(int course) {
        visited[course] = 1;
        for(int i : edges[course]){
            if(visited[i]==0){
                dfs(i);
                if(isCycle) return ;
            } else if (visited[i]==1) {
                isCycle = true;
                return ;
            }
        }
        visited[course] = 2;
    }
};