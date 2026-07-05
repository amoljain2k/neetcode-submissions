class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        left,right = 0, len(heights)-1
        while left<right:
            h = min(heights[left], heights[right])
            b = right-left
            curr = h*b
            best = max(best, curr)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return best
        