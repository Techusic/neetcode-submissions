class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ass = dict()
        k = len(heights)-1
        i = 0
        while True:
            ass.setdefault((k-i)*min(heights[i], heights[k]),[i,k])
            if heights[i] <= heights[k]:
                i = i+1
            elif heights[i] > heights[k]:
                k = k-1
            if i == len(heights)-1 :
                break
        return max(ass)