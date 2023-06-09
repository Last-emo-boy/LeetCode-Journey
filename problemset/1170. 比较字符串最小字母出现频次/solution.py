from typing import List
import bisect

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            return s.count(min(s))
        
        f_words = sorted(f(word) for word in words)
        res = []

        for query in queries:
            f_query = f(query)
            res.append(len(f_words) - bisect.bisect_right(f_words, f_query))

        return res