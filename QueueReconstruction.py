# An algorithm to reconstruct the queue.
# Suppose you have a random list of people standing in a queue.
# Each person is described by a pair of integers (h,k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h.

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        ans = []
        for pep in people:
            ans.insert(pep[1], pep)
            
        return ans
