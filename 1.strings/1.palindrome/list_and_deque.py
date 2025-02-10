# https://leetcode.com/problems/valid-palindrome/
import collections


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # str_list = list()
        str_deque = collections.deque()
        for c in s.lower():
            if c.isalnum():
                str_deque.append(c)

        while len(str_deque) > 1:
            if str_deque.pop() != str_deque.popleft():
                return False
        return True
