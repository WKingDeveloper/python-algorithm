# https://leetcode.com/problems/group-anagrams/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet_dict = {chr(letter): 0 for letter in range(ord("a"), ord("z") + 1)}
        words = []

        for str in strs:
            init_value = alphabet_dict.copy()
            for c in str:
                init_value[c] += 1

            value = ""
            for k, v in init_value.items():
                if v != 0:
                    value += f"{k}{v}"
            words.append({str: value})

        generate_dict = dict()
        for word in words:
            for k, v in word.items():
                generate_dict.setdefault(v, []).append(k)

        return list(generate_dict.values())
