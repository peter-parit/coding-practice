'''
Given an array of integers nums containing n + 1 integers where each 
integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and using only constant extra space.

NOTE: This question is simple to do with O(n) space. Below is O(1) space.
'''
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        
        # starting point
        slow = nums[0]
        fast = nums[nums[0]]

        # find intersection
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # find where the cycle starts
        slow = 0 
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        # return number with duplicate value
        return slow