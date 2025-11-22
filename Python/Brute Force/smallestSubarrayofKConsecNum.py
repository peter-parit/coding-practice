'''
Given an array arr, return the smallest size of subarray with k consecutive numbers.
arr contains the number from 1 to n (size of arr) -- all of them are unique.
arr = [7, 3, 4, 6, 9, 5, 8, 2, 1], k = 5 --> 6 (because [7, 3, 4, 6, 9, 5] with 3, 4, 5, 6, 7)

[1, 2, 3, 4, 5, 6, 7, 8, 9] -- [8, 7, 1, 2, 5, 3, 0, 6, 4]
'''
class Solution:
    
    def smallestSubarray(nums: list[int], k: int) -> int:
        
        map = {num: i for i, num in enumerate(nums)}
        
        sorted_lst = sorted(nums)
        smallest_subarray = len(nums) + 1
        
        for i in range(0, len(nums) - k + 1):
            
            min_index = len(nums) + 1
            max_index = -1
            
            for num in sorted_lst[i: i + k]:
                min_index = min(min_index, map[num])
                max_index = max(max_index, map[num])
            
            smallest_subarray = min(smallest_subarray, max_index - min_index + 1)
        
        return smallest_subarray
    
# TODO: might not be correct, need testing.