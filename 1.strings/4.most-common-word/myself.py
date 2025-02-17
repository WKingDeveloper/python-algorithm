# https://leetcode.com/problems/most-common-word/
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        paragraph = paragraph.lower()

        paragraph = re.sub("[!?',;.]", " ", paragraph)

        word_dict = dict()
        most_word = tuple()

        max_num = 0

        for word in paragraph.split():
            if word in banned:
                continue

            print(f"word : {word}")
            word_dict.setdefault(word, 0)
            word_dict[word] += 1
            num = word_dict[word]

            if num > max_num:
                most_word = (word, word_dict[word])
                max_num = num

        return most_word[0]
