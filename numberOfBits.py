class Solution:
    def numberOfBits(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1 # AND 1 // XOR ^ 
            n >> 1 #Right shift  // << Left Right
        return res