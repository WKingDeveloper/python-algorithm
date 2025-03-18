# https://leetcode.com/problems/palindrome-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head.next
        heads = [head.val]
        if node == None:
            return True

        while node != None:
            value = node.val
            heads.append(value)
            node = node.next

        left = 0
        right = len(heads) - 1
        while right > left:
            if heads[left] != heads[right]:
                return False
            left += 1
            right -= 1

        return True
