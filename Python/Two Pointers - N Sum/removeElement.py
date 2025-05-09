class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # base cases
        if len(nums) == 0: return 0
        if len(nums) == 1:
            return 0 if nums[0] == val else 1

        # set pointers
        right = len(nums) - 1
        left = 0
        k = len(nums)
        while (left <= right):
            # if target, 'remove' element from k
            if nums[left] == val:
                k -= 1
                # swap left with right when right is not target
                while (left < right and nums[right] == val): 
                    right -= 1
                    k -= 1
                nums[left] = nums[right]
                right -= 1
            left += 1
        
        return k