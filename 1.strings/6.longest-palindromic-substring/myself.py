# https://leetcode.com/problems/longest-palindromic-substring/
# 풀다 실함. 규칙성과 재귀를 구현하지 못함.
from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        is_even = len(s) % 2 == 0
        quotient = len(s) // 2

        max_str = ""
        if is_even == False:
            num = quotient
            while num > 1:
                str = ""

                is_same = True
                while is_same:
                    for i in range(1, num + 1):
                        str_before = s[num - i]
                        str_after = s[num + i]
                        is_same = str_before == str_after
                        if is_same:
                            str += f"{str_before}{str}{str_after}"
                            if len(max_str) < len(str):
                                max_str = str
                num -= 1

            while num < len(s):
                num = quotient
                str = ""

                is_same = True
                while is_same:
                    for i in range(1, num + 1):
                        str_before = s[num - i]
                        str_after = s[num + i]
                        is_same = str_before == str_after
                        if is_same:
                            str += f"{str_before}{str}{str_after}"
                            if len(max_str) < len(str):
                                max_str = str
                num += 1
            return max_str
