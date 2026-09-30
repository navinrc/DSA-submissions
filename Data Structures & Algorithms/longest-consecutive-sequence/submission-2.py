class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hs = set(nums)

        for n in hs:
            if (n - 1) not in hs:
                length = 0
                while (n + length) in hs:
                    length += 1
                longest = max(longest, length)
        return longest