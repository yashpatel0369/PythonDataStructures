# Given a string s and a string t, a function to check if s is subsequence of t.
# A subsequence of a string is a new string which is formed from the original string from deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in s:
            if char not in t:
                return False
            t = t[(t.index(char) + 1):]
        return True
