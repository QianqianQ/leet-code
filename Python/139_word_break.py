class Solution:
    def wordBreak(self, s, wordDict):
        # cache[i] is True if there is a valid sequence up until s[:i]
        self.cache = [False for _ in range(len(s)+1)]
        self.d = set(wordDict)
        
        self.cache[0] = True
        
        for end in range(0, len(s)+1):
            for start in range(0, end):
                if self.cache[start] and s[start:end] in self.d:
                    self.cache[end] = True
                    continue

        dp = (len(s)+1)*[False]
        dp[0] = True
        wd = set(wordDict)
        for i in range(len(s)):
            for j in range(i+1):
                if dp[j] and s[j:i+1] in wd:
                    dp[i+1] = True
        return dp[-1]


if __name__=="__main__":
    solution = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(solution.wordBreak(s,wordDict))


    s = "applepenapple" 
    wordDict = ["apple", "pen"]
    print(solution.wordBreak(s,wordDict))



    s = "catsandog" 
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(solution.wordBreak(s,wordDict))

    print(set(wordDict))
