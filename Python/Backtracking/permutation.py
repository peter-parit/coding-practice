'''
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
'''
class Solution:
    
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        # storing all answers
        perms = []
        
        # total length to achieve when backtracking
        n = len(nums)
        
        # help track if number is in the permutation already or not
        used = [False] * n

        def backtrack(curr: list[int]):
            
            # length reached
            if len(curr) == n:
                perms.append(curr[:])
                return
            
            # for all starting values
            for i in range(n):
                
                #if not used yet
                if not used[i]:
                    used[i] = True
                    
                    # append number to permutation
                    curr.append(nums[i])
                    
                    # continue
                    backtrack(curr)
                    
                    # remove number, backtracking to another number
                    curr.pop()
                    
                    # reset because number is taken out
                    used[i] = False
            
        # start with nothing
        backtrack([])
        
        # final answer
        return perms