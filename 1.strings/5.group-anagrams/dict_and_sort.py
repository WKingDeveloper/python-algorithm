# https://leetcode.com/problems/group-anagrams/
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for str in strs:
            sort_str = "".join(sorted(str))
            answer[sort_str].append(str)

        return list(answer.values())
