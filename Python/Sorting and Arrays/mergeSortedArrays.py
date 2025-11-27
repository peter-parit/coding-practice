'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. To accommodate this, 
nums1 has a length of m + n, where the first m elements denote the 
elements that should be merged, and the last n elements are set to 0 
and should be ignored. nums2 has a length of n.
'''
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # index for full array
        i_mn = len(nums1) - 1
        # index for nums1
        i_m = m - 1
        # index for nums2
        i_n = n - 1

        # process starts from the end for O(m + n)
        # if nums2 is not fully read
        while i_n >= 0:
            # if nums1 is not fully read and nums1 index is greater than nums2 index
            if i_m >= 0 and nums1[i_m] > nums2[i_n]:
                # make the full array's current index nums1
                nums1[i_mn] = nums1[i_m]
                i_m -= 1
            else:
                # make the full array's current index nums2
                nums1[i_mn] = nums2[i_n]
                i_n -= 1
            # move to next index
            i_mn -= 1
