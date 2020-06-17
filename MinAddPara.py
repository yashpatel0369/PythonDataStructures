# A function to count the minimum number of parantheses needed to make the string valid.
# Given a string S of '(' and ')' parantheses, we add the minimum number of parantheses ('(' or ')', and in any position) so that the resulting parantheses string is valid.

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        count = 0
        for s in S:
            if s == "(":
                stack.append(s)
            if s == ")":
                if stack:
                    stack.pop(-1)
                elif not stack:
                    count += 1
            
        return count + len(stack)
