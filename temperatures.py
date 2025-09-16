from typing import List
class Solution:
    def dailyTemp(self, temperatures: List[int]) -> List[int]:
        results = [0]*len(temperatures)
        stack = []
        
        for i, tmp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < tmp:
                index = stack.pop
                results[index] = i-index
            stack.append(i)
        return results
                