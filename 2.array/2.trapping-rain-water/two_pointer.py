# https://leetcode.com/problems/trapping-rain-water/

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        answer = 0

        while left < right:
            left_max, right_max = max(height[left], left_max), max(
                height[right], right_max
            )

            if left_max <= right_max:
                answer += left_max - height[left]
                left += 1
            else:
                answer += right_max - height[right]
                right -= 1

        return answer
