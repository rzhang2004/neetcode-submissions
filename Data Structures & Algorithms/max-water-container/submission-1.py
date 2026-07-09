class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        max_fill = 0

        while l < r:
            max_fill = max(max_fill, (r-l) * min(heights[r], heights[l]))

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_fill


