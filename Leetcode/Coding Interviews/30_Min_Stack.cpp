/*
注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
调用 min、push 及 pop 的时间复杂度都是 O(1)。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.

提示：
    各函数的调用总次数不超过 20000 次
*/
#include <iostream>
#include <stack>
using namespace std;

class MinStack {
private:
    stack<int> stk;
    stack<int> min_stk;
public:
    /** initialize your data structure here. */
    MinStack() {}
    
    void push(int x) {
        stk.push(x);
        if (min_stk.empty() || x <= min_stk.top()){
            min_stk.push(x);
        }
    }
    
    void pop() {
        if (stk.empty()) return ;
        int t = stk.top();
        stk.pop();
        if (t == min_stk.top()){
            min_stk.pop();
        }
    }
    
    int top() {
        return stk.top();
    }
    
    int min() {
        return min_stk.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->min();
 */