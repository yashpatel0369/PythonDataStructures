# A function to initialize stack of size n and increment botton k elements by val.
# The following operations are performed on the stack: push, pop and inc.
# Push: Adds x to the top of the stack if the stack hasn't reached the maxSize.
# Pop: Retures the top of the stack or -1 if the stack is empty.
# Inc: Increments the bottom k elements in the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.count = 0
        self.msize = maxSize

    def push(self, x: int) -> None:
        if self.count < self.msize:
            self.stack.append(x)
            self.count += 1

    def pop(self) -> int:
        if self.stack:
            self.count -= 1
            return self.stack.pop(-1)
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i < len(self.stack):
                self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
