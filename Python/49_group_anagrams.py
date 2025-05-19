from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        if len(strs) == 1:
            return [strs]
        for s in strs:
            reorder_s = ''.join(sorted(s))
            anagrams[reorder_s].append(s)
        res = [anagrams[reorder_s] for reorder_s in anagrams]
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
