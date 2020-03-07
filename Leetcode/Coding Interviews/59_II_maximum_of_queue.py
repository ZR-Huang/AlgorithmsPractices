'''
请定义一个队列并实现函数 max_value 得到队列里的最大值，
要求函数max_value、push_back 和 pop_front 的时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

Example 1:
Input: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
Output: [null,null,null,2,1,2]

Example 2:
Input:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
Output: [null,-1,-1]

Constraints:
- 1 <= push_back,pop_front,max_value的总操作数 <= 10000
- 1 <= value <= 10^5
'''
from collections import deque
class MaxQueue:

    def __init__(self):
        self.Q = list()
        self.help_q = deque()

    def max_value(self) -> int:
        return self.help_q[0] if self.help_q else -1


    def push_back(self, value: int) -> None:
        self.Q.append(value)
        while self.help_q and self.help_q[-1] < value:
            self.help_q.pop()
        self.help_q.append(value)


    def pop_front(self) -> int:
        if not self.Q:
            return -1
        if self.Q[0] == self.help_q[0]:
            self.help_q.popleft()
        return self.Q.pop(0)

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()