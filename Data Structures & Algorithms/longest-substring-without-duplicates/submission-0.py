class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        state = {}
        max_length = 0

        for end in range(len(s)):
            state[s[end]] = state.get(s[end], 0) + 1
            # we contract the window by reducing the start by 1 / removing it if 0
            # until there is a valid length of chars in the map
            while state[s[end]] > 1:
                state[s[start]] -= 1
                if state[s[start]] == 0:
                    del state[s[start]]
                start += 1
            
            max_length = max(max_length, end - start + 1)
        
        return max_length
