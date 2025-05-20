class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        def sorting_func(log):
            if log[-1].isnumeric():
                return (1,)

            identifier, contents = log.split(' ', 1)
            return (0, contents, identifier)

        return sorted(logs, key=sorting_func)


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.reorderLogFiles(
            [
                "dig1 8 1 5 1",
                "let1 art can",
                "dig2 3 6",
                "let2 own kit dig",
                "let3 art zero"
            ]
        )
    )
