'''
Given an array of integers nums, return the length of the longest consecutive sequence 
of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 
greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
'''
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        # add all numbers to starting set
        starting = set()
        result = 0
        for num in nums:
            starting.add(num)

        # iterate over num and find starting numbers, then get its
        # consecutive sequence
        for num in nums:

            # num is starting if num exists and num - 1 doesn't exist
            # (smallest available starting num)
            if num in starting and (num - 1) not in starting:
                
                # start counting its sequence
                current = num
                count = 0
                while current in starting:
                    starting.remove(current)

                    current += 1
                    count += 1
                
                # store the max
                result = max(result, count)
        
        return result

