from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # 将区间按照左端点从小到大、右端点从大到小的顺序进行排序
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        # 将查询和它的原始索引一起放入一个列表，然后按照查询的大小进行排序
        queries = sorted((q, i) for i, q in enumerate(queries))
        
        # 创建一个空的优先队列，用于存储区间
        queue = []
        
        # 初始化结果数组
        res = [0] * len(queries)
        
        # 初始化区间的指针
        i = 0
        
        # 对每一个查询，将所有可以包含该查询的区间放入优先队列中，然后将队列顶部所有无法使用的区间删除，
        # 最后将队列顶部的区间长度放入结果数组中
        for q, j in queries:
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(queue, (r - l + 1, r))
                i += 1
            while queue and queue[0][1] < q:
                heapq.heappop(queue)
            res[j] = queue[0][0] if queue else -1
        
        return res