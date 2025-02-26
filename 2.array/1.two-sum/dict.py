# https://leetcode.com/problems/two-sum/description/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, v in enumerate(nums):
            dict[i] = v

        for i, v in enumerate(nums):
            if target - v in dict.values() and target - v != i:
                return [i, dict[nums[i + 1 :].index(target - v)]]
