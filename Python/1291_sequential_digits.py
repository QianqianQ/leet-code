class Solution:
    def sequentialDigits_old(self, low: int, high: int) -> list[int]:
        str_low, str_high = str(low), str(high)
        low_no_digits, high_no_digits = len(str_low), len(str_high)

        res = []

        for digit_n in range(low_no_digits, high_no_digits + 1):
            for i in range(10):
                new_num = str(i)
                valid = True
                for j in range(digit_n - 1):
                    new_digit = int(new_num[-1]) + 1
                    if new_digit > 9:
                        valid = False
                        break
                    new_num += str(int(new_num[-1]) + 1)
                if not valid:
                    continue
                int_new_num = int(new_num)
                if low <= int_new_num <= high and int_new_num not in res:
                    res.append(int_new_num)
                if int_new_num > high:
                    break
        return res

    def sequentialDigits(self, low: int, high: int) -> list[int]:
        ans = []

        for i in range(1, 10):
            num = i
            next_digit = i + 1

            while num <= high and next_digit <= 9:
                num = num * 10 + next_digit
                if low <= num <= high:
                    ans.append(num)
                next_digit += 1

        ans.sort()
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.sequentialDigits(100, 300))
    print(solution.sequentialDigits_old(100, 300))
