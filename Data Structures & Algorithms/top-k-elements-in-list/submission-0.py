class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {n:0 for n in nums}
        result = []
        for n in nums:
            freqMap[n] += 1
        for key in freqMap:
            if freqMap[key] >= k:
                result.append(key)
        return result
