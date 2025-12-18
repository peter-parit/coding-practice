class Solution:
    def trap(self, height: list[int]) -> int:
        
        n = len(height)
        if n == 0: return 0
        
        leftMax = [0] * n
        rightMax = [0] * n
        result = 0
        
        # tallest block in the left at the current position
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        
        # tallest block in the right at the current position
        rightMax[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
            
        # calculate how much water can be held with the min height between left/right
        # and the current position height
        for i in range(n):
            result += min(leftMax[i], rightMax[i]) - height[i]
            
        return result