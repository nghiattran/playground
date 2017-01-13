import math

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        base = 0xffffffff
        return n ^ base