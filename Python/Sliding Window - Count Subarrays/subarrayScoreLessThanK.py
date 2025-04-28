'''The score of an array is defined as the product of its sum and its length.
Given a positive integer array nums and an integer k, return the number of 
non-empty subarrays of nums whose score is strictly less than k.'''
class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        count, left, right, score = 0, 0, 0, 0

        while right < len(nums):
            score += nums[right]

            while left <= right and score * (right - left + 1) >= k:
                score -= nums[left]
                left += 1
            
            count += right - left + 1
            right += 1
        
        return count