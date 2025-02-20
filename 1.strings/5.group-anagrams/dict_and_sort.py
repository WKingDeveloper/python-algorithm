# https://leetcode.com/problems/group-anagrams/
from typing import List
from collections import defaultdict

# TODO : 팀소트 정렬에 대해 알아보기


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for str in strs:
            sort_str = "".join(sorted(str))
            answer[sort_str].append(str)

        return list(answer.values())
