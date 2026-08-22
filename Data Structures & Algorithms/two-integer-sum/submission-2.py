class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap approach - one pass
        #so we are not looking at same ele twice
        #we are looking only at previously seen ele from prevMap
        #time: O(n)
        #space: O(n)
        prevMap = {} # val: index
        for i,n in enumerate(nums):
            complement = target - n
            if complement in prevMap:
                return [prevMap[complement], i]
            prevMap[n] = i
        return []