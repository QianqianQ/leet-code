class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        def dfs(i, j):
            if (i < 0 or i >= len(grid) or
                    j < 0 or j >= len(grid[0]) or
                    grid[i][j] != '1'):
                return
            grid[i][j] = '#'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)

        return num_islands


if __name__ == "__main__":
    solution = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(solution.numIslands(grid))
