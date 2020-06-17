# A function to remove the outermost parantheses of every primitive string in the primitive decomposition of S.
# A valid parantheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parantheses strings and + represnets string concatenation.
# For example, "", "()", "(())()", and "(()(()))" are all valid parantheses strings.
# A valid parantheses string S is primitive if it is non empty, and there does not exist a way to split it into S = A + B, with A and B nonempty valid parantheses strings.
# Given a valid parantheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parantheses strings.

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        temp = ""
        ans = ""
        i = 0
        j = 0
        for s in S:
            if s == '(':
                i += 1
            else:
                j += 1
            temp += s
            if i == j:
                ans += temp[1:len(temp)-1]
                temp = ""
        return ans
