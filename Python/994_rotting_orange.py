class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        timer = 0
        while fresh:
            if not rotting:
                return -1
            rotting = {
                (i + di, j + dj) for i, j in rotting
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]
                if (i + di, j + dj) in fresh
            }
            fresh -= rotting
            timer += 1
        return timer


if __name__ == "__main__":
    # Example usage
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    solution = Solution()
    result = solution.orangesRotting(grid)
    print(result)  # Output: 4
