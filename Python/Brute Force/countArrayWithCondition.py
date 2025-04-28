'''Given an integer array nums, return the number of subarrays of length 3 
such that the sum of the first and third numbers equals exactly half of the second number.'''
class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        count = 0
        for i in range(0, len(nums) - 2):
            if (nums[i] + nums[i + 2]) == (nums[i + 1] / 2):
                count += 1

        return count