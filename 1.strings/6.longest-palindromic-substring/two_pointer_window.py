# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:

    def longestPalindrome(self, s: str) -> str:
        result = ""

        if len(s) < 2 or (s == s[::-1]):
            return s

        for i in range(len(s) - 1):
            result = max(
                result,
                self.expand(s, i, i + 1),
                self.expand(s, i, i + 2),
                key=len,
            )

        return result

    def expand(self, s: str, left: int, right: int) -> str:
        result = s[left]
        while left > 0 and right < len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
            result = s[left, right + 1]
        return result
