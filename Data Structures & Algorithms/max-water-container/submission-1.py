class Solution:
    def maxArea(self, heights: List[int]) -> int:
        k = len(heights)-1
        i = 0
        ass = 0
        while True:
            ass = max(ass, (k-i)*min(heights[i], heights[k]))

            if heights[i] <= heights[k]:
                i = i+1
            elif heights[i] > heights[k]:
                k = k-1
            if i == len(heights)-1 :
                break
        return ass