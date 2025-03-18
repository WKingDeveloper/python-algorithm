# https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional, ListNode


class Solution:

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        nodes = []

        if list1:
            list1_val, list1_next = list1.val, list1.next
            nodes.append(list1_val)
        else:
            list1_val, list1_next = None, None

        while list1_next:
            nodes.append(list1_next.val)
            if list1_next.next:
                list1_next = list1_next.next
            else:
                break

        if list2:
            list2_val, list2_next = list2.val, list2.next
            nodes.append(list2_val)
        else:
            list2_val, list2_next = None, None

        while list2_next:
            nodes.append(list2_next.val)
            if list2_next.next:
                list2_next = list2_next.next
            else:
                break
        print(f"list2_next end")
        nodes.sort()

        def generateListNode(nodes: List) -> Optional[ListNode]:
            list_node = None
            while len(nodes) > 0:
                return ListNode(nodes.pop(0), generateListNode(nodes))
            return list_node

        answer = generateListNode(nodes)

        return answer

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
