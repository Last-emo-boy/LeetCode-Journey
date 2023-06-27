from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        res = dp1 = dp2 = arr[0]
        for i in range(1, n):
            dp1, dp2 = max(dp1 + arr[i], arr[i]), max(dp2 + arr[i], dp1)
            res = max(res, dp1, dp2)
        return res