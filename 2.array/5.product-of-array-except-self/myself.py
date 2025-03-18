# https://leetcode.com/problems/product-of-array-except-self/submissions/1567444411/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        m1 = 1
        m2 = 1

        zero_count = 0
        if m1 == 0:
            zero_count = 1

        for num in nums:
            if num == 0:
                zero_count += 1
            if num != 0:
                m2 *= num
            m1 *= num

        for num in nums:
            if num == 0 and zero_count == 1:
                answer.append(m2)
                continue
            if num == 0 and zero_count > 1:
                answer.append(0)
                continue
            answer.append(m1 // num)

        return answer
