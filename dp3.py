from typing import List
class Solution:
    def maxSteal(self, values: List[int]) -> int:
        if not values:
            return 0
        
        one_before = 0
        two_before = 0
        
        for n in values:
            temp = max(n+ two_before, one_before)
            two_before = one_before
            one_before = temp
            
        return one_before
        
sol = Solution()
print(sol.maxSteal([1, 5, 1, 1, 9]))