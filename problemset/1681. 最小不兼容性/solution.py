class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        c = n // k
        count = [0] * 17
        for num in nums:
            count[num] += 1
            if count[num] > k:
                return -1

        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        valid = []
        for mask in range(1, 1 << n):
            if bin(mask).count('1') == c:
                subset = [nums[i] for i in range(n) if (mask >> i) & 1]
                if len(subset) == len(set(subset)):
                    valid.append(mask)
                    dp[mask] = max(subset) - min(subset)

        for mask in range(1, 1 << n):
            if bin(mask).count('1') % c == 0:
                subset = [v for v in valid if (v & mask) == v]
                for sub in subset:
                    dp[mask] = min(dp[mask], dp[mask ^ sub] + dp[sub])

        return dp[-1] if dp[-1] != float('inf') else -1