class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        def generate_new_nums(new_nums):
            if len(new_nums) == 1:
                return new_nums[0]
            temp_new_nums = []
            for i in range(len(new_nums) - 1):
                temp_new_nums.append((new_nums[i] + new_nums[i + 1]) % 10)
            return generate_new_nums(temp_new_nums)

        return generate_new_nums(nums)


if __name__ == '__main__':
    # Example usage
    nums = [2, 5, 3, 9]
    solution = Solution()
    result = solution.triangularSum(nums)
    print(result)  # Output: 5