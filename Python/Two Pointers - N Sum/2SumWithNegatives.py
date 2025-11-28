class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        # hashmap to the original index for each number
        arr = [(num, i) for i, num in enumerate(nums)]
        
        # sort the numbers
        arr.sort()

        left = 0
        right = len(nums) - 1
        
        # two pointers
        while left < right:
            s = arr[left][0] + arr[right][0]
            # if more than target, move down from right
            if s > target:
                right -= 1
            # if less than target, move up from left
            elif s < target:
                left += 1
            # else, return the sorted 2 indices
            else:
                return sorted([arr[left][1], arr[right][1]])
        
        return []