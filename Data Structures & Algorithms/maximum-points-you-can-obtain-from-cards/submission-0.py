class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_points = sum(cardPoints)
        max_points = 0
        start = 0
        current_window_points = 0  # state
        if k == len(cardPoints):
            return total_points
        for end in range(len(cardPoints)):
            current_window_points += cardPoints[end]

            if end - start + 1 == len(cardPoints) - k:
                max_points = max(max_points, total_points - current_window_points)
                current_window_points -= cardPoints[start]
                start += 1
        return max_points
