class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        # worst soln
        for i in range(0,len(nums)):
            for j in range(len(nums)-1, i, -1):
                if nums[i] + nums[j] == target:
                    indices.append(i)
                    indices.append(j)
        return indices