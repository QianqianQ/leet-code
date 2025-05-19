import math
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        n = len(nums)
        range_sum = 0
        for i, v in enumerate(nums):
            min_val, max_val = math.inf, -math.inf
            for j in range(i, n):
                max_val = max(max_val, nums[j])
                min_val = min(min_val, nums[j])
                range_sum += max_val - min_val
        return range_sum


if __name__ == "__main__":
    solution = Solution()
    print(solution.subArrayRanges([1, 2, 3]))
