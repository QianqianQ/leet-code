class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            length = 0 
            return length

        sub_length = []
        sub_list = []
        sub_string = ""
        for c in s:
            if c not in sub_list:
                sub_list.append(c)
            else:
                i = sub_list.index(c)
                sub_string = "".join(sub_list)
                sub_length.append(len(sub_list))
                sub_list=sub_list[i+1:]
                sub_list.append(c)

        sub_length.append(len(sub_list))
        if sub_string=="":
            return len(sub_list)

        return max(sub_length)

if __name__ == "__main__":
    str1 = "abcabcbb"
    str2 = "bbbbb"
    str3 = "pwwkew"
    str4 = "c"
    str5 = "aab"
    str6 = "dvdf"
    sub1 = Solution().lengthOfLongestSubstring(str1)
    sub2 = Solution().lengthOfLongestSubstring(str2)
    sub3 = Solution().lengthOfLongestSubstring(str3)
    sub4 = Solution().lengthOfLongestSubstring(str4)
    sub5 = Solution().lengthOfLongestSubstring(str5)
    sub6 = Solution().lengthOfLongestSubstring(str6)

    print(sub1,sub2,sub3,sub4,sub5,sub6)
