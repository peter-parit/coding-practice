'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
'''
# My Solution:
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1
        
        freq_map = sorted(freq_map.items(), key = lambda item: item[1], reverse = True)
        result = []
        for num, _ in freq_map:
            result.append(num)
            if len(result) == k:
                return result

# Video's Solution
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        count = {}
        freqMap = [[] for i in range(len(nums) + 1)]
        
        # count frequency of elements
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # insert value to the index which corresponds to its count
        for num, count in count.items():
            freqMap[count].append(num)
            
        result = []
        
        # from the highest count, append values to result
        for i in range(len(freqMap) - 1, 0, -1):
            currentList = freqMap[i]
        
            # add all values with that count to result
            for num in currentList:
                result.append(num)
            
            # returns when k is reached
            if len(result) == k: 
                return result
        

        