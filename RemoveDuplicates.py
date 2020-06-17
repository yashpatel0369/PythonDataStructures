# A function to repeatedly remove duplicates until we no longer can.
# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for s in S:
            if stack:
                if stack[-1] == s:
                    stack.pop(-1)
                else:
                    stack.append(s)
            elif not stack:
                stack.append(s)
                
        return "".join(stack)
