'''
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = int((left + right) / 2)
            current = nums[mid]
            if current < target:
                left = mid + 1
            elif current > target:
                right = mid - 1
            else:
                return mid
        
        if target <= nums[left]: return left 
        else: return left + 1