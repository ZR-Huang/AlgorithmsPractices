/*
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]
Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 
Constraints:
Methods pop, top and getMin operations will always be called on non-empty stacks.
*/
#include <iostream>
#include <stack>
using namespace std;

class MinStack {
public:
    /** initialize your data structure here. */
    stack<int> s, min_stack;
    MinStack() {
        
    }
    
    void push(int x) {
        s.push(x);
        if(min_stack.empty() || x <= min_stack.top()) min_stack.push(x);
    }
    
    void pop() {
        int pop_elem = s.top();
        s.pop();
        if(!min_stack.empty() && pop_elem == min_stack.top()) min_stack.pop();
    }
    
    int top() {
        return !s.empty() ? s.top() : NULL;
    }
    
    int getMin() {
        return !min_stack.empty() ? min_stack.top() : NULL;
    }
};

int main(){
    MinStack* obj = new MinStack();
    obj->push(3);
    obj->push(2);
    int param3 = obj->top();
    int param2 = obj->getMin();
    obj->pop();
}
/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */