# Recuirsion + Backtracking
# Time Complexity: O(4^n / sqrt(n))
# Space Complexity: O(n)
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        Generates all combinations of well-formed parentheses.

        Args:
            n (int): The number of pairs of parentheses.

        Returns:
            list[str]: A list of strings, each representing a valid
                combination of parentheses.
        """
        def dfs(left, right, s):
            if left + right == n * 2:
                res.append(s)
                return

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.generateParenthesis(3)
    print(result)  # Output: ['((()))', '(()())', '(())()', '()(())', '()()()']
