# non LC

class Solution:
    def maxSum(self, nums: list[int], k: int):
        start = 0
        windowed_sum = 0
        max_sum = float('-inf')

        for end in range(len(nums)):
            windowed_sum += nums[end]

            if end - start + 1 == k:
                max_sum = max(max_sum, windowed_sum)
                windowed_sum -= nums[start]
                start += 1

        return max_sum
