# https://leetcode.com/problems/palindrome-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections
from typing import Optional, ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        heads = collections.deque()
        node = head.next
        heads.append(head.val)
        if node == None:
            return True

        while node != None:
            value = node.val
            heads.append(value)
            node = node.next

        while len(heads) > 1:
            if heads.popleft() != heads.pop():
                return False

        return True
