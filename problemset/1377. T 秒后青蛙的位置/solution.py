from collections import defaultdict

class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        graph = defaultdict(list)
        for u, v in edges:
            u, v = u-1, v-1
            graph[u].append(v)
            graph[v].append(u)

        visited = [False]*n
        prob = [0]*n
        prob[0] = 1.0

        def dfs(node, time):
            unvisited_count = sum(not visited[i] for i in graph[node])
            if time < t and unvisited_count == 0:
                if node == target - 1:
                    return prob[node]
                return 0
            if node == target - 1 and time == t:
                return prob[node]
            visited[node] = True
            for child in graph[node]:
                if not visited[child]:
                    prob[child] = prob[node] / unvisited_count
                    result = dfs(child, time + 1)
                    if result > 0:
                        return result
            return 0

        return dfs(0, 0)