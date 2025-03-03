# https://leetcode.com/problems/trapping-rain-water/

# 못풀었음
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        tmp_num = 0
        for i, h1 in enumerate(height):
            if h1 == 0 or i < tmp_num:
                continue
            if i == len(height) - 1:
                break
            num = 0
            for j, h2 in enumerate(height[i + 1 :]):

                if h2 >= h1:
                    print(
                        f"i : {i}, j : {j}, h1 : {h1}, h2 : {h2}, j*h1 : {j*h1 }, num : {num}"
                    )
                    print(f"j*h1 - num : {j*h1 + num}")
                    add = j * h1 + num
                    answer += add
                    print(f"answer : {answer}")
                    tmp_num = i + j + 1
                    break
                else:
                    num += h2 * -1
        return answer
