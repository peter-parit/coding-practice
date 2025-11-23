'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where 
the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
'''
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        result = []
        
        def backtrack(start, current, total):
            # if reached target number
            if total == target:
                # add candidate and stop
                result.append(current[:])
                return
            # if exceeds, fails and return to previous state
            if total > target:
                return
            
            # iterate through candidates
            for i in range(start, len(candidates)):
                # add candidate in
                current.append(candidates[i])
                # continue onward on the same number and updated total
                backtrack(i, current, total + candidates[i])
                # revert back to original state + prepare to add in another candidate
                current.pop()
                
        # start at index 0, empty, and total of 0
        backtrack(0, [], 0)        
        return result