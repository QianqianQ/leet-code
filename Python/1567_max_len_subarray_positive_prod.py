class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        positive, negative, ans = 0, 0, 0

        for num in nums:
            if num == 0:
                positive, negative = 0, 0
            elif num > 0:
                positive += 1
                negative = negative + 1 if negative > 0 else 0
            else:
                # swap positive and negative counts
                temp = positive
                positive = negative + 1 if negative > 0 else 0
                negative = temp + 1

            ans = max(ans, positive)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.getMaxLen([1, -2, -3, 4]))  # Output: 4
