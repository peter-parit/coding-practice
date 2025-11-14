'''
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, you may move to 
either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
'''
class Solution:

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # memoization
        n = len(triangle)
        memo = {}
        
        def dp(i, j):
            # if at the last row, return value
            if i == n - 1: return triangle[i][j]
            
            # if in memo, retrun
            if (i, j) in memo: return memo[(i, j)]
            
            # get value choosing the one below
            down = dp(i + 1, j)
            
            # get value of choosing the one down right
            diag = dp(i + 1, j + 1)
            
            # store the best path for that value (dp = current + best choice)
            memo[(i, j)] = triangle[i][j] + min(down, diag)
            
            # return stored value
            return memo[(i, j)]
        
        return dp(0, 0) # memo[(0, 0)] stores the min path