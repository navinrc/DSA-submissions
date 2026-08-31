class Solution:
    """
    return -> list of lists of all distinct triplets, 
    if no triplets satisfy sum 0 -> ret empty list
    1. brute for gives - O(n^3) time, recommended is O(n^2) time and O(1) space
    
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        #[-4,-1,-1,0,1,2]
        for i, val in enumerate(nums):
            if i > 0 and nums[i-1] == val:
                continue
            l,r = i + 1, len(nums) - 1
            
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([val,nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res             
