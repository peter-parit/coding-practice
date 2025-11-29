'''
Given an integer array nums, return an array output where output[i] is the product 
of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(n) time without using the division operation?
Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]
'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] *= output[i] * prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * suffix
            suffix *= nums[i]

        return output