from typing import List
from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        h, seen, m, n = [], set(), len(mat), len(mat[0])
        indices = [0] * m
        value = sum(mat[i][0] for i in range(m))
        heappush(h, (value, indices))
        seen.add(tuple(indices))

        while k > 0:
            value, indices = heappop(h)
            k -= 1

            for i in range(m):
                if indices[i] < n - 1:
                    new_indices = list(indices)
                    new_indices[i] += 1
                    if tuple(new_indices) not in seen:
                        seen.add(tuple(new_indices))
                        new_value = value - mat[i][indices[i]] + mat[i][new_indices[i]]
                        heappush(h, (new_value, new_indices))

        return value