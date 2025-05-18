from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        char_counter = Counter(s)
        char_heap = [(-count, char) for char, count in char_counter.items()]
        heapq.heapify(char_heap)

        if -char_heap[0][0] > (len(s) + 1) // 2:
            return ''

        prev_count, prev_char = 0, ''

        while char_heap:
            neg_count, char = heapq.heappop(char_heap)
            res.append(char)

            if prev_count < 0:
                heapq.heappush(char_heap, (prev_count, prev_char))
            neg_count += 1
            prev_count, prev_char = neg_count, char

        res = ''.join(res)
        if len(res) != len(s):
            return ''

        return res


if __name__ == "__main__":

    s = "aab"
    solution = Solution()
    result = solution.reorganizeString(s)
    print(result)  # Output: "aba"
    s = "aaab"
    result = solution.reorganizeString(s)
    print(result)  # Output: ""
