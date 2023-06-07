import heapq
from typing import List

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        # 构造得分差数组
        rewardDiff = [(reward1[i] - reward2[i], i) for i in range(n)]
        # 使用贪心算法选择得分差最大的奶酪给第一只老鼠吃
        rewardDiff.sort()
        total = 0
        for _ in range(n - k):
            _, idx = heapq.heappop(rewardDiff)
            total += reward2[idx]
        for _ in range(k):
            _, idx = heapq.heappop(rewardDiff)
            total += reward1[idx]
        return total