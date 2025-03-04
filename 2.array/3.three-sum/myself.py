# https://leetcode.com/problems/3sum/


# timeout 코드
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        negatives, zeros, positives = [], [], []
        for num in nums:
            if num < 0:
                negatives.append(num)
            elif num > 0:
                positives.append(num)
            else:
                zeros.append(num)
        positives.sort(reverse=True)

        num_dict = {}
        answer = []
        for i, n_num in enumerate(negatives):
            for j, p_num in enumerate(positives):
                if (
                    n_num + p_num == 0
                    and len(zeros) > 0
                    and [n_num, 0, p_num] not in answer
                ):
                    answer.append([n_num, 0, p_num])
                    num_dict[n_num] = True
                elif (
                    n_num + p_num < 0
                    and j < len(positives) - 1
                    and [n_num, p_num, abs(n_num + p_num)] not in answer
                ):
                    if abs(n_num + p_num) in positives[j + 1 :]:
                        answer.append([n_num, p_num, abs(n_num + p_num)])
                        num_dict[n_num] = True
                elif (
                    n_num + p_num > 0
                    and i < len(negatives) - 1
                    and [n_num, (n_num + p_num) * -1, p_num] not in answer
                ):
                    if (n_num + p_num) * -1 in negatives[i + 1 :]:
                        answer.append([n_num, (n_num + p_num) * -1, p_num])
                        num_dict[n_num] = True
        if len(zeros) > 2:
            answer.append([0, 0, 0])

        return answer
