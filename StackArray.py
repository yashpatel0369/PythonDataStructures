# Given an array target and integer n, a function to return the list of operations need to meet the target array.
# The following are the operations which can be performed on the stack: push and pop.

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        ops = []
        for i in range(1, n+1):
            if stack == target:
                break
            if i in target:
                stack.append(i)
                ops.append("Push")
            if i not in target:
                stack.append(i)
                ops.append("Push")
                stack.remove(i)
                ops.append("Pop")
        return ops
