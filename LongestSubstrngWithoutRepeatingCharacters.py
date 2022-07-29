class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == len(s):
            return len(s)
        if len(set(s)) == 1:
            return 1
        substring = ""
        substr_len = 1
        for i in s:
            if i not in substring:
                substring = substring + i
                substr_len = max(substr_len, len(substring))
            else:
                substring = substring.split(i)[1] + i
        return substr_len

s= Solution()
print(s.lengthOfLongestSubstring("puiofnfppp"))
print(s.lengthOfLongestSubstring("puiofnqwer"))
print(s.lengthOfLongestSubstring("hhhhhhhhhh"))