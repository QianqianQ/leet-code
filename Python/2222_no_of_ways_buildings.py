from collections import Counter

class Solution:
    def numberOfWays(self, s: str) -> int:
        num_counter = Counter(s)
        num_occur_counter= {'0': 0, '1': 0}
        res = 0
        for i in range(len(s)):
            if s[i] == '1':
                res += num_occur_counter['0'] * num_counter['0']
                num_counter['1'] -= 1
                num_occur_counter['1'] += 1
            else:
                res += num_occur_counter['1'] * num_counter['1']
                num_counter['0'] -= 1
                num_occur_counter['0'] += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfWays("001101"))  # Output: 6
    print(s.numberOfWays("11100"))   # Output: 0
