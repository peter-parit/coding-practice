'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        # sort array for searching
        nums.sort()

        i = 0
        n = len(nums)
        result: list[list[int]] = []

        # i acts as outermost pointer
        while (i < n - 2):

            # move to the last repeated value
            if ((i > 0) and nums[i] == nums[i - 1]):
                i += 1
                continue
            j = i + 1
            k = n - 1

            # two pointer
            while (j < k):
                total = nums[i] + nums[j] + nums[k]
                if (total > 0):
                    k -= 1
                elif (total < 0):
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1

                    # move to last repeated value
                    while ((j < k) and (nums[j] == nums[j - 1])): 
                        j += 1

            # if first number > 0, then the sum of 3 numbers will always be > 0
            if (nums[i] > 0): return result
            i += 1
            
        return result
    
    
# attempt 2:
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        result: list[list[int]] = []

        if nums[0] > 0: return list(result)

        n = len(nums)
        for i in range(n - 2):
            s = nums[i]
            if (i > 0 and s == nums[i - 1]):
                continue
            j = i + 1
            k = n - 1

            while j < k:
                left = nums[j]
                right = nums[k]

                if (s + left + right) > 0:
                    k -= 1
                if (s + left + right) < 0:
                    j += 1
                if (s + left + right) == 0:
                    result.append([s, left, right])
                    j += 1

                    while ((j < k) and nums[j] == nums[j - 1]):
                        j += 1
        
        return result


