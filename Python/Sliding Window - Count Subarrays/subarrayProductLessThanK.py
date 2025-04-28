'''Given an array of integers nums and an integer k, return the number of contiguous subarrays 
where the product of all the elements in the subarray is strictly less than k.'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:

        if k <= 1: return 0

        count = 0
        total = 1

        left = 0
        for right in range(0, len(nums)):
            total *= nums[right]
            while left < right and total >= k:
                total /= nums[left]
                left += 1
            if total < k: count += (right - left + 1)
        
        return count