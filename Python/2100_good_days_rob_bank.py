class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        n = len(security)

        if time == 0:
            return list(range(n))

        non_increasing = [0] * n
        non_decreasing = [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                non_increasing[i] = non_increasing[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                non_decreasing[i] = non_decreasing[i + 1] + 1

        res = []
        for i in range(time, n - time):
            if non_increasing[i] >= time and non_decreasing[i] >= time:
                res.append(i)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.goodDaysToRobBank([5, 3, 3, 3, 5, 6, 2], 2))
