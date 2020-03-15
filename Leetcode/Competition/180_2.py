class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.curr_len = 0

    def push(self, x: int) -> None:
        if self.curr_len < self.maxSize:
            self.stack.append(x)
            self.curr_len += 1

    def pop(self) -> int:
        if self.curr_len > 0:
            self.curr_len -= 1
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        k = min([self.curr_len, k])
        for i in range(k):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)