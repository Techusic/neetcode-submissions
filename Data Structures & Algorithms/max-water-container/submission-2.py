class Solution:
    def maxArea(self, heights: List[int]) -> int:
        k = len(heights)-1
        i = 0
        ass = 0
        while i < k:
            ass = max(ass, (k-i)*min(heights[i], heights[k]))

            if heights[i] <= heights[k]:
                i = i+1
            else:
                k = k-1
        return ass