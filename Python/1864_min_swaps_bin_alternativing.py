# Time: O(n)
# Space: O(1)
class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        digit_counter = {"0": 0, "1": 0}

        digit_counter["0"] = s.count("0")
        digit_counter["1"] = n - digit_counter["0"]

        # impossible to create an alternating string
        if abs(digit_counter["1"] - digit_counter["0"]) > 1:
            return -1

        def count_swaps(start_char):
            swaps = 0

            for c in s:
                if c != start_char:
                    swaps += 1
                start_char = "1" if start_char == "0" else "0"
            return swaps // 2

        swap_start_0 = count_swaps("0")
        swap_start_1 = count_swaps("1")

        # even-length
        if len(s) % 2 == 0:
            return min(swap_start_0, swap_start_1)

        # odd-length
        return (swap_start_0
                if digit_counter["0"] > digit_counter["1"]
                else swap_start_1)


if __name__ == "__main__":
    solution = Solution()
    print(solution.minSwaps("111000"))
