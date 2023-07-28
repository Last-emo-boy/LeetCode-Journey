from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        for prev, next in relations:
            graph[prev].append(next)
            in_degree[next] += 1

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = time[i - 1]

        queue = deque()
        for i in range(1, n + 1):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                dp[next_course] = max(dp[next_course], dp[course] + time[next_course - 1])
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return max(dp)