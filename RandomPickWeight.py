# Given an array w of positive integers, where w[i] describes the weight of index i, a function pickIndex which randomly picks an index in proportion to its weight.
# The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments.
# Arguments are always wrapped in a list, even if there aren't any.

import random

class Solution:

    def __init__(self, w: List[int]):
        self.w = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        return random.choices(range(len(self.w)), cum_weights=self.w)[0]
