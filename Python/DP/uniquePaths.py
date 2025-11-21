'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach 
the bottom-right corner.
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # create default m x n grid
        dp = [[1] * n for _ in range(m)]
        
        # accumulate walks until the end starting from 1, 1
        for i in range(1, m):
            for j in range(1, n):
                
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                                 
        # final count               
        return dp[m - 1][n - 1]
            
            
            

        