"""
Given two arrays A[] and B[] consisting of N integers where A[i] represents the initial position of the ith plane
and B[i] is the speed at which the plane is landing, the task is to print the number of the plane that can be stopped
from landing by shooting an aircraft at every second.

Examples:

Input: A[] = {1, 3, 5, 4, 8}, B[] = {1, 2, 2, 1, 2}
Output: 4
Explanation:
    At second 1, shoot the plane at index 0, the positions of the planes are now A[] = {_, 1, 3, 3, 6}.
    At second 2, shoot the plane at index 1, the positions of the planes are now A[] = {_, _, 1, 2, 4}.
    At second 3, shoot the plane at index 2, the positions of the planes are now A[] = {_, _, _, 1, 2}.
    At second 4, shoot the plane at index 4 or 5, the positions of the planes are now A[] = {_, _, _, _, _}.
    Therefore, a total of 4 planes can be stopped from landing.

Input: A[] = {2, 8, 2, 3, 1}, B[] = {1, 4, 2, 2, 2}
Output: 2
"""


class Solution:
    # my greedy attempt
    def maximizePlanes(self, A: list[int], B: list[int]) -> int:
        import math

        A = A.copy()
        B = B.copy()
        count = 0

        # while exists plane flying
        while max(A) > 0:
            closest = math.inf
            index = -1

            for i, plane in enumerate(A):
                # plane's next position -> determining which one dies faster
                next = plane - B[i]

                # if found one that dies faster
                if next < closest and plane > 0:
                    closest = next
                    index = i

            # if found a plane
            if index != -1:
                # set the plane as inf aka. dead
                A[index] = -int(math.inf)

                # increase plane count
                count += 1

            # proceed to time n + 1
            A = [A[i] - B[i] for i in range(len(A))]
        return count

    # claude given
    def maxPlanes(self, A: list[int], B: list[int]) -> int:
        import math

        # Calculate landing time for each plane: ceil(position / speed)
        # Store as (landing_time, speed, index)
        planes = []
        for i in range(len(A)):
            if B[i] > 0:  # Only consider planes that are moving
                landing_time = math.ceil(A[i] / B[i])
                planes.append(landing_time)

        # Sort by landing time
        planes.sort()

        count = 0
        current_second = 1

        for landing_time in planes:
            # Can we shoot this plane before it lands?
            if current_second <= landing_time:
                count += 1
                current_second += 1  # We shoot at this second

        return count
