# https://leetcode.com/problems/two-sum/description/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        values = []
        is_same = False
        for i, v in enumerate(nums):
            print(f"v : {v}, target-v : {target-v} ")
            if target - v in nums[i + 1 :]:
                values.append(v)
                values.append(target - v)
                if v == target - v:
                    is_same = True
                break

        answer = []
        print(f"values : {values}")
        if is_same:
            for i, v in enumerate(nums):
                if v == values[0]:
                    answer.append(i)
                    if len(answer) == 2:
                        break
        else:
            answer.append(nums.index(values[0]))
            answer.append(nums.index(values[1]))
        return answer
