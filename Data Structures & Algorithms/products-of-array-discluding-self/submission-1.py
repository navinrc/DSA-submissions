class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        prefix_product = [1] * len(nums)
        suffix_product = [1] * len(nums)

        for i in range(len(nums)):
            prefix_product[i] = (prefix_product[i - 1] if i != 0 else 1) * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            suffix_product[i] = (suffix_product[i + 1] if i != len(nums) - 1 else 1) * nums[i]

        for i in range(len(nums)):
            if i == 0:
                result.append(1 * suffix_product[i + 1])
            elif i == len(nums) - 1:
                result.append(prefix_product[i - 1] * 1)
            else:
                result.append(prefix_product[i - 1] * suffix_product[i + 1])
        return result
