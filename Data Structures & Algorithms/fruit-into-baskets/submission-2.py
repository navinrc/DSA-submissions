class Solution:
    """
    As per NC sliding window II, we do not shrink the window until valid.
    Instead, we move forward directly as we only care about valid window size always.
    """
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        state = {} # curr window
        max_fruits = 0 # result

        for end in range(len(fruits)):
            state[fruits[end]] = state.get(fruits[end], 0) + 1

            if len(state) > 2:
                state[fruits[start]] -= 1
                if state[fruits[start]] == 0:
                    del state[fruits[start]]
                start += 1
            
            max_fruits = max(max_fruits, sum(state.values())) # end - start + 1 is valid too, as each index represents only 1 fruits
        return max_fruits

