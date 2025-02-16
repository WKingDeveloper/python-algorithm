# https://leetcode.com/problems/reorder-data-in-log-files/
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = list()
        digits = list()

        for log in logs:
            if log.split()[1].isnumeric():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda logs: (logs.split()[1:], logs.split()[0]))
        return letters + digits
