# https://leetcode.com/problems/array-partition/description/

from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                answer += num
        return answer
