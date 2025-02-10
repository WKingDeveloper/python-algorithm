# https://leetcode.com/problems/valid-palindrome/
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = s.lower()
        str = re.sub("[^a-z0-9]", "", str)

        str_reverse = str[::-1]

        if str == str_reverse:
            return True

        return False
