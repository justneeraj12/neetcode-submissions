class Solution:
    def maxArea(self, heights):
        max_area = 0
        R = len(heights) -1 
        L = 0

        while L <  R:
            width = R - L
            min_height = min(heights[R], heights[L])
            curr_area = width * min_height

            max_area = max(curr_area, max_area)

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return max_area
        