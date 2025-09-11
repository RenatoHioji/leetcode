from typing import List
class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        #2 números somados = target
        n = len(nums)
        dict = {}
        for i in range(0, n):
            if nums[i] in dict:
                return [dict.get(nums[i]), i]
            dict[target-nums[i]] = i
        return -1

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))