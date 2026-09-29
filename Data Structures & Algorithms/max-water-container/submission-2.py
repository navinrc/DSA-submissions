class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        cur_area = 0
        left, right = 0, len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            cur_area = width * height

            max_area=max(max_area,cur_area)

            if heights[left] < heights[right]:
                left += 1
            # elif heights[left] > heights[right] or heights[left] == heights[right]:
            else:
                right -= 1
            
        return max_area