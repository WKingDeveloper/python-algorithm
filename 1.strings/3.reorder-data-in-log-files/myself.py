# https://leetcode.com/problems/reorder-data-in-log-files/
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        answer = []
        letter_dict = dict()
        digit_list = list()

        for identifier_log in logs:
            split_log = identifier_log.split(" ", 1)
            identifier = split_log[0]
            log = split_log[1]

            if log[0].isnumeric():
                digit_list.append({identifier: log})

            else:
                letter_dict.setdefault(log, []).append(identifier)

        letter_keys = list(letter_dict.keys())
        letter_keys.sort()

        for key in letter_keys:
            identifiers = letter_dict[key]
            identifiers.sort()

            for identifier in identifiers:
                identifier_log = identifier + " " + key
                answer.append(identifier_log)

        for value in digit_list:
            for identifier, log in value.items():
                identifier_log = identifier + " " + log
                answer.append(identifier_log)

        return answer
