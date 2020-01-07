'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
	push(x) -- Push element x onto stack.
	pop() -- Removes the element on top of the stack.
	top() -- Get the top element.
	getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''
from collections import deque
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = deque()
        self.s2 = deque()
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        if not self.s2:
            self.s2.append(x)
        elif x <= self.s2[-1]:
            self.s2.append(x)


    def pop(self) -> None:
        x = self.s1.pop()
        if self.s2 and x == self.s2[-1]:
            self.s2.pop()


    def top(self) -> int:
        return self.s1[-1] if self.s1 else None


    def getMin(self) -> int:
        return self.s2[-1] if self.s2 else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()