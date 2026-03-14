from typing import (
    List,
)


class Solution:
    """
    @param arr: the arithmetic progression array
    @return: the missing number
    """

    # Time complexity: O(n)
    # Space complexity: O(1)
    def missing_number(self, arr: List[int]) -> int:
        n = len(arr)
        diff = (arr[-1] - arr[0]) // n
        for i in range(0, n):
            if arr[i] + diff != arr[i + 1]:
                return arr[i] + diff

        return -1

    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def missing_number1(self, arr: List[int]) -> int:
        n = len(arr)
        diff = (arr[-1] - arr[0]) // n
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            expected = arr[0] + m * diff
            if arr[m] == expected:  # there is no missing number up to mid
                l = m + 1
            else:
                r = m - 1

        return arr[r] + diff  # or arr[0] + (r + 1) * diff
