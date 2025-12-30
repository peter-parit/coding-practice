'''
Basic Binary Search
'''
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        # set the pointers
        left = 0
        right = len(nums) - 1

        # binary search
        while left <= right:
            
            mid = (left + right) // 2

            if nums[mid] < target: left = mid + 1       # current number is greater than target
            elif nums[mid] > target: right = mid - 1    # current number is lesser than target
            else: return mid                            # current number is the target
            
        return -1                                       # not found