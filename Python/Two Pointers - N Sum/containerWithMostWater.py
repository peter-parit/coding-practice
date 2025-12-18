'''You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.'''
class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxA = 0
        left = 0
        right = len(height) - 1

        # two pointer
        while left != right:
            currentA = min(height[left], height[right]) * abs(right - left)
            maxA = max(currentA, maxA)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxA
    
    
# attempt 2
class Solution:
    def maxArea(self, heights: list[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        max_container = 0
        
        while left < right:
            c_left = heights[left]
            c_right = heights[right]
            d = right - left
            
            if c_left < c_right:
                max_container = max(max_container, d * c_left)
                left += 1
            else:
                max_container = max(max_container, d * c_right)
                right -= 1
            
        return max_container