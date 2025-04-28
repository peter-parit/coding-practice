'''Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.'''
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        if len(nums) == 3: return sum(nums)

        # sort list for better search
        nums.sort()

        bestSum = nums[0] + nums[1] + nums[2]
        i = 0

        # outermost pointer
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1

            # two pointer
            while j < k:
                currentSum = nums[i] + nums[j] + nums[k]
                if currentSum > target:
                    k -= 1
                elif currentSum < target:
                    j += 1
                else: return currentSum
                if abs(currentSum - target) < abs(bestSum - target):
                    bestSum = currentSum
            i += 1
        return bestSum